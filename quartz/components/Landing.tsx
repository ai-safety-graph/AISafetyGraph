import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import landingStyle from './styles/landing.scss'
import Search from "./Search"


export default (() => {
  const SearchComponent = Search()
  function Landing(componentData: QuartzComponentProps) {
    return (
      <div>
        <SearchComponent {... componentData}/>
        <div class="content-container">
          <p class="landing-header">Landing Page</p>
        </div>
      </div>
    )
  }

  Landing.css = landingStyle
  return Landing
}) satisfies QuartzComponentConstructor