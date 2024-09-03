import { QuartzComponentConstructor } from "./types"
import landingStyle from './styles/landing.scss'


export default (() => {
  function Landing() {
    return (
      <div>
        <div class="content-container">
          <p class="landing-header">Landing Page</p>
        </div>
      </div>
    )
  }

  Landing.css = landingStyle
  return Landing
}) satisfies QuartzComponentConstructor