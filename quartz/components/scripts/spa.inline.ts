import micromorph from "micromorph"

// adapted from `micromorph`
// https://github.com/natemoo-re/micromorph

const NODE_TYPE_ELEMENT = 1
let announcer = document.createElement('route-announcer')
const isElement = (target: EventTarget | null): target is Element => (target as Node)?.nodeType === NODE_TYPE_ELEMENT
const isLocalUrl = (href: string) => {
  try {
    const url = new URL(href)
    if (window.location.origin === url.origin) {
      if (url.pathname === window.location.pathname) {
        return !url.hash
      }
      return true
    }
  } catch (e) { }
  return false
}

const getOpts = ({ target }: Event): { url: URL, scroll?: boolean } | undefined => {
  if (!isElement(target)) return
  const a = target.closest("a")
  if (!a) return
  if ('routerIgnore' in a.dataset) return
  const { href } = a
  if (!isLocalUrl(href)) return
  return { url: new URL(href), scroll: 'routerNoscroll' in a.dataset ? false : undefined }
}

function notifyNav(slug: string) {
  const event = new CustomEvent("spa_nav", { detail: { slug } })
  document.dispatchEvent(event)
}

let p: DOMParser
async function navigate(url: URL, isBack: boolean = false) {
  p = p || new DOMParser()
  const contents = await fetch(`${url}`)
    .then((res) => res.text())
    .catch(() => {
      window.location.assign(url)
    })
  if (!contents) return;
  if (!isBack) {
    history.pushState({}, "", url)
    window.scrollTo({ top: 0 })
  }
  const html = p.parseFromString(contents, "text/html")
  let title = html.querySelector("title")?.textContent
  if (title) {
    document.title = title
  } else {
    const h1 = document.querySelector('h1')
    title = h1?.innerText ?? h1?.textContent ?? url.pathname
  }
  if (announcer.textContent !== title) {
    announcer.textContent = title
  }
  announcer.dataset.persist = ''
  html.body.appendChild(announcer)

  micromorph(document.body, html.body)

  // now, patch head 
  const elementsToRemove = document.head.querySelectorAll(':not([spa-preserve])')
  elementsToRemove.forEach(el => el.remove())
  const elementsToAdd = html.head.querySelectorAll(':not([spa-preserve])')
  elementsToAdd.forEach(el => document.head.appendChild(el))

  notifyNav(document.body.dataset.slug!)
  delete announcer.dataset.persist
}

function createRouter() {
  if (typeof window !== "undefined") {
    window.addEventListener("click", async (event) => {
      const { url } = getOpts(event) ?? {}
      if (!url) return
      event.preventDefault()
      try {
        navigate(url, false)
      } catch (e) {
        window.location.assign(url)
      }
    })

    window.addEventListener("popstate", () => {
      if (window.location.hash) return
      try {
        navigate(new URL(window.location.toString()), true)
      } catch (e) {
        window.location.reload()
      }
      return
    })
  }
  return new class Router {
    go(pathname: string) {
      const url = new URL(pathname, window.location.toString())
      return navigate(url, false)
    }

    back() {
      return window.history.back()
    }

    forward() {
      return window.history.forward()
    }
  }
}

createRouter()

if (!customElements.get('route-announcer')) {
  const attrs = {
    'aria-live': 'assertive',
    'aria-atomic': 'true',
    'style': 'position: absolute; left: 0; top: 0; clip: rect(0 0 0 0); clip-path: inset(50%); overflow: hidden; white-space: nowrap; width: 1px; height: 1px'
  }
  customElements.define('route-announcer', class RouteAnnouncer extends HTMLElement {
    constructor() {
      super()
    }
    connectedCallback() {
      for (const [key, value] of Object.entries(attrs)) {
        this.setAttribute(key, value)
      }
    }
  })
}
