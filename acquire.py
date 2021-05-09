"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""

import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from requests import get

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = ['r-spacex/SpaceX-API',
'jesusrp98/spacex-go',
'bradtraversy/spacex_launch_stats',
'r-spacex/spacexstats-react',
'arjunyel/angular-spacex-graphql-codegen',
'llSourcell/Landing-a-SpaceX-Falcon-Heavy-Rocket',
'EmbersArc/gym-rocketlander',
'haroldadmin/MoonShot',
'shahar603/SpaceXtract',
'treyhuffine/graphql-react-typescript-spacex',
'rodolfobandeira/spacex',
'SpaceXLaunchBot/SpaceXLaunchBot',
'lukeify/spacex-reddit-css',
'NITJSR-OSS/My-SpaceX-Console',
'arex18/rocket-lander',
'joshuaferrara/SpaceX',
'lazywinadmin/SpaceX',
'r-spacex/launch-timeline',
'DaniruKun/spacex-iss-docking-sim-autopilot',
'mbertschler/dragon-iss-docking-autopilot',
'hyperloop/hyperloop',
'shahar603/Telemetry-Data',
'SpaceXLand/api',
'OMIsie11/SpaceXFollower',
'TheAlphamerc/flutter_spacexopedia',
'EduD/front-challenge-spacex',
'ItsCalebJones/SpaceLaunchNow-Android',
'SaidBySolo/SpaceXPy',
'vinayphadnis/SpaceX-Python',
'romebell/ga-spacex-frontend',
'BaderEddineOuaich/spacex_stellar',
'manhdv96/SpaceX-Kernel-Exynos7420',
'Alric/spacex',
'romebell/ga-spacex-api',
'rikkertkoppes/spacex-telemetry',
'HiKaylum/SpaceX-PY',
'tdrach/Sciview',
'RoryStolzenberg/spacexstats',
'Hyp-ed/hyped-2019',
'ghelobytes/mission-control',
'sparky8512/starlink-grpc-tools',
'candydasein/spacex-launches',
'SaraJo/SpaceXGMail',
'emersonlaurentino/spacex-qraphql-api',
'SpaceXLand/client',
'SophieDeBenedetto/spacex-apply',
'moesalih/spacex.moesalih.com',
'VGVentures/spacex_demo',
'codersgyan/spacex-redesign',
'JohnnySC/SpaceX',
'IJMacD/spacex-launches',
'brunolcarli/Ark',
'tipenehughes/space-x-app',
'pushpinderpalsingh/SpaceDash',
'orcaman/spacex',
'Illu/moonwalk',
'R4yGM/SpaceXTelemetry-Api',
'jesusrp98/space-curiosity',
'shahar603/Launch-Dashboard-API',
'sudharsan-selvaraj/selenium-spacex-docking',
'zlsa/f9r-v2',
'SteveSunTech/stardust',
'koxm/MMM-SpaceX',
'santiaguf/spacex-platzi',
'alshapton/SpacePY-X',
'looksocii/SpaceX_PSIT-Project',
'DirectMyFile/DiffuseSpace',
'badreddine-dlaila/spacex-app-demo',
'codexa/SpaceX-Rocket',
'ivanddm/spacexapp',
'andrnors/flutter-101-spaceX',
'djtimca/HASpaceX',
'lukacs-m/SpaceXMVVMSwiftUICombine',
'zwenza/spacexnow',
'danopstech/starlink_exporter',
'BrianIshii/git-falcon9',
'sdsubhajitdas/Rocket_Lander_Gym',
'imranhsayed/graphql-react-app',
'Eliminater74/SpaceX-Pure',
'asicguy/spacex_uart',
'samisharafeddine/SpaceXAPI-Swift',
'ayybradleyjh/kOS-Hoverslam',
'openland/spacex',
'Goldob/iss_docking_automation',
'jvsinghk/spacex',
'ugurkanates/SpaceXReinforcementLearning',
'HanSolo/touchjoystick',
'colbyfayock/my-spacex-launches',
'wilkerlucio/pathom-connect-spacex',
'Hyp-ed/hyped-2018',
'DanielRings/ReusableLaunchSystem',
'RomanSytnyk/SpaceX-App-unofficial',
'louisjc/spacexlaunches.com',
'AkiaCode/spacex-api.js',
'Ionic-SpaceX/SpaceX',
'JohannesFriedrich/SpaceX',
'R4yGM/SpaceXNews-api',
'akim3235/spacex-apollo-graphql',
'goncharom/SpaceXRocket',
'r-spacex/api-style-guide',
'ahmetakil/spacex_graphql',
'ElvinC/Dragon-docker',
'PiotrRut/SpaceX-Launches',
'schmidgallm/spaceXwatch',
'Thomas-Smyth/SpaceX-API-Wrapper',
'Elucidation/ThrustVectorControl',
'IainCole/SpaceXVideoApp',
'michaellyons/react-launch-gauge',
's-ai-kia/SpaceXland',
'gregv/meeting-timeline',
'sroaj/spacexfm',
'reidbuckingham48/spacex-nasa-flight-data',
'matdziu/SpaceXMVI',
'ryansan/SpaceX-Design',
'ergenekonyigit/spacex-cljs',
'JAQ-SpaceX/spaceX-brief',
'XiaoTeTech/spacex.xiaote.com',
'Tearth/Oddity',
'patrickyin/kotlin-coroutines-vs-rx',
'doflah/boostback',
'PatrykWojcieszak/X-Info',
'MITHyperloopTeam/software_core',
'airesvsg/spacex',
'Tearth/InElonWeTrust',
'ALuxios/SpaceX',
'leoge0113/SpaceX-Web',
'Patrykz94/kOS-RTLS-Landing',
'harisudhan7889/SpaceX',
'jamesgeorge007/spacex-launcher-stats',
'BekaAM/spaceX',
'499602D2/tg-launchbot',
'phch/ucdavis-hyperloop',
'syedsadiqali/sapient-spacex-app',
'shashidhark/Spacex-API-Frontend',
'peetck/spacex-explorer',
'SirKeplan/spacex-reddit-wiki',
'AndrewRLloyd88/mb-career-accelerator-spaceX',
'victorshinya/spacex-rockets',
'enciyo/SpaceX',
'crunchysoul/spacex_ex',
'bbutler522/SpaceX-Visualization',
'odziem/fetch-deno',
'ahmetmvural1/SpaceXProject',
'janipalsamaki/spacex-robot',
'alexgtn/spacex-api-wrapper',
'oplS16projects/SpaceXplore',
't-ozeren/SpaceXData',
'andrey-leshenko/ISSDockingBotGame',
'dongzerun/nice-spacex',
'mikkrieg/spaceXAPI',
'elricdog/SpaceX-StarShip',
'jiachengzhang1/spacex-and-mars',
'jesusrp98/bot-hackathon-spacex',
'developer-junaid/SpaceX-App',
'faiza203/SpaceX',
'richiemccoll/visualising-front-end-performance-demo',
'ozonni/SpotTheFire',
'svipatov/spacex-tracker',
'pmborg/SpaceX-RO-Falcons',
'me-aakash-online/spaceX-launch-program',
'ping-n/spaceX-js-app',
'zlsa/spacex-info',
'joshuadeguzman/spacex-land',
'ShinteiMai/next-spacex',
'BriantOliveira/SpaceX-Dataset',
'spacexksp/spacexksp.github.io',
'Sheldon1538/SpaceXApp',
'tejalkotkar/Mission_SpaceX',
'mattmillsxyz/x-watch',
'staszewski/spacex-api-app',
'ronal2do/Graphql-SpaceX-API',
'ayberkgerey/SpaceX_Data_Retrofit',
'cmoir97/SpaceX-App',
'rinoldm/SBURB',
'abh80/spacexapp',
'jor-dan/SpaceX-GraphQL',
'mcastorena0316/react-redux-capstone',
'jackkoppa/go-for-launch',
'Emmanuel1118/Crew-Dragon-Autopilot',
'AzuxDario/Marsy'

]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)