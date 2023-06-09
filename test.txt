<!DOCTYPE html>
<!-- saved from url=(0049)https://intranet.hbtn.io/projects/2122#task-19425 -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

    <title>Project: Python - Exceptions | Holberton Montevideo, Uruguay Intranet</title>

      <link rel="stylesheet" href="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/application-de7a7629d7e9640180b0bd919b4bc71b09a95eea8de57184c10a3e56be89c558.css">
      <script async="" src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/analytics.js.download"></script><script src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/loader.js.download"></script>
      <script src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/application-e21faf8b39b08f079e6f186b7f20cee159b8e1733e4fe43492cdfed21c44b2db.js.download"></script>
      <link rel="shortcut icon" type="image/x-icon" href="https://intranet.hbtn.io/favicon.ico">
      <meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="HABlw2q0hdL9WOY8-cawkjaJy6lNU6nr9dNYnTaxLooXsS8DzeBMnaiakv9eQiuxkuyt-FOhiTvwNHJn5pDPoQ">

      <link rel="apple-touch-icon" href="https://intranet.hbtn.io/apple-touch-icon.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

      <!-- intro.js for interactive onboarding -->
        <script src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/intro.min.js.download"></script>
        <link rel="stylesheet" media="screen" href="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/introjs.min.css">

      <!-- React -->
      <script src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/application-f19103cc6405403aa3f6.js.download"></script>
      <link rel="stylesheet" media="screen" href="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/application-87456da7.css">

  </head>

  <body class="
    signed_in
    env_production
    
    " translate="no" data-theme-suffix="" data-checker-special-theme="pride_month">

      <input type="hidden" id="hbtn-slack-url" value="https://holberton-school-org.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="https://intranet.hbtn.io/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>


    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="" data-original-title="Projects"><a href="https://intranet.hbtn.io/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My reports"><a href="https://intranet.hbtn.io/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="QA Reviews I can make"><a href="https://intranet.hbtn.io/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Evaluation quizzes"><a href="https://intranet.hbtn.io/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="" data-original-title="Concepts"><a href="https://intranet.hbtn.io/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="" data-original-title="Conference rooms"><a href="https://intranet.hbtn.io/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Servers"><a href="https://intranet.hbtn.io/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="" data-original-title="Sandboxes"><a href="https://intranet.hbtn.io/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Video on demand"><a href="https://intranet.hbtn.io/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Peers"><a href="https://intranet.hbtn.io/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Captain&#39;s Logs"><a href="https://intranet.hbtn.io/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain's Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Officers"><a href="https://intranet.hbtn.io/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Speakers of the Day"><a href="https://intranet.hbtn.io/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com/">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Profile">
    <a href="https://intranet.hbtn.io/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url(&#39;https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/006/305/thumb/patricio_benglian_1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230608%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230608T161405Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=35de415aeb078bb347d929005ede91b9e201815815ab4deeb3cf3364c14db43b&#39;)"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="https://intranet.hbtn.io/">
    <div class="logo"></div>
</a>
  <ul>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>


    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="" data-original-title="Projects"><a href="https://intranet.hbtn.io/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My reports"><a href="https://intranet.hbtn.io/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="QA Reviews I can make"><a href="https://intranet.hbtn.io/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Evaluation quizzes"><a href="https://intranet.hbtn.io/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="" data-original-title="Concepts"><a href="https://intranet.hbtn.io/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="" data-original-title="Conference rooms"><a href="https://intranet.hbtn.io/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Servers"><a href="https://intranet.hbtn.io/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="" data-original-title="Sandboxes"><a href="https://intranet.hbtn.io/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Video on demand"><a href="https://intranet.hbtn.io/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Peers"><a href="https://intranet.hbtn.io/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Captain&#39;s Logs"><a href="https://intranet.hbtn.io/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain's Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Officers"><a href="https://intranet.hbtn.io/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Speakers of the Day"><a href="https://intranet.hbtn.io/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com/">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Profile">
    <a href="https://intranet.hbtn.io/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url(&#39;https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/006/305/thumb/patricio_benglian_1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230608%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230608T161405Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=35de415aeb078bb347d929005ede91b9e201815815ab4deeb3cf3364c14db43b&#39;)"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
      <div id="layout-bars">
        
        <div class="px-5 py-3" id="student-switch-curriculum">
  <div class="dropdown d-flex flex-column gap-1">
    <span class="fs-small text-muted">Curriculum</span>

    <div aria-haspopup="true" aria-expanded="false" class="align-items-center d-flex gap-3" data-toggle="dropdown" id="student-switch-curriculum-dropdown" role="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-600">
          Foundations v2 - Part 2
        </span>
        <span class="fs-small text-muted">
          Average: <span class="fw-500">100.0%</span>
        </span>
      </div>

      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa fa-angle-up  fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa fa-angle-down  fa-fw"></i>
        </span>
      </div>
    </div>

    <ul aria-labelledby="student-switch-curriculum-dropdown" class="dropdown-menu fs-5">
        <li>
          <a href="https://intranet.hbtn.io/curriculums/208/observe">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                  Foundations v2 - Part 1
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">93.11%</span>
                </span>
              </div>

            </div>
</a>        </li>
        <li>
          <a href="https://intranet.hbtn.io/curriculums/252/observe">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                  Foundations v2 - Part 2
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">100.0%</span>
                </span>
              </div>

                <span class="fw-600 text-info" style="margin-left: 42px">
                  <i aria-hidden="true" class="fa fa-check "></i>
                </span>
            </div>
</a>        </li>
    </ul>
  </div>
</div>

        
        
        
      </div>

      <article class="">

        
<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <div class="sm-gap">
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Amateur&quot;,&quot;author&quot;:&quot;Guillaume&quot;,&quot;weight&quot;:1,&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;,&quot;correction&quot;:{&quot;released&quot;:true,&quot;requires_manual_correction&quot;:false}},&quot;project&quot;:{&quot;completion&quot;:100.0,&quot;id&quot;:2122,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Exceptions&quot;,&quot;score&quot;:{&quot;mandatory&quot;:100.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:3},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"><div class="panel panel-tile project-header"><div class="panel-body" style="align-items: center; display: flex;"><div class="pathway" style="padding: 16px;"><div class="project-circle project-circle-on-tile" style="border-radius: 100%; height: 150px; margin: auto; padding: 5px; width: 150px;"><div data-test-id="CircularProgressbarWithChildren"><div style="position: relative; width: 100%; height: 100%;"><svg class="CircularProgressbar " viewBox="0 0 100 100" data-test-id="CircularProgressbar" style="height: 140px; vertical-align: middle; width: 140px;"><path class="CircularProgressbar-trail" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 0px;"></path><path class="CircularProgressbar-path" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 0px;"></path></svg><div data-test-id="CircularProgressbarWithChildren__children" style="position: absolute; width: 100%; height: 100%; margin-top: -100%; display: flex; flex-direction: column; justify-content: center; align-items: center;"><div style="height: 100%; position: absolute; transform: rotate(0turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div style="height: 100%; position: absolute; transform: rotate(0.333333turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div style="height: 100%; position: absolute; transform: rotate(0.666667turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div class="position-relative"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Python - Exceptions"><div class="align-items-center d-flex justify-content-center project-circle-body active" style="border-radius: 100%; height: 124px; width: 124px;"><img alt="Project badge" src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png" width="60%"></div></span><div class="p-1 position-absolute project-circle-score text-center" style="border-radius: 10px; width: 125px;"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Score of Mandatory Tasks"><span class="d-block">100%</span></span></div></div></div></div></div></div></div><div class="project-info" style="flex-basis: 100%; margin: 16px;"><h1 style="margin: 0px;">Python - Exceptions</h1><ul class="list-group metadata" id="project-metadata"><li class="list-group-item"><i aria-hidden="true" class="fa fa-level-up fa-fw"></i> Amateur</li><li class="list-group-item"><i aria-hidden="true" class="fa fa-user fa-fw"></i> By: Guillaume</li><li class="list-group-item"><i aria-hidden="true" class="fa fa-cog fa-fw"></i> Weight: 1</li><li class="list-group-item"><i aria-hidden="true" class="fa fa-check-square fa-fw"></i> Your score will be updated as you progress.</li></ul></div></div></div></div>
  </div>



    <div id="project_id" style="display: none" data-project-id="2122"></div>



      

      

      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://intranet.hbtn.io/rltoken/WxV68L6c_WRMEzZt8P7oIA" title="Errors and Exceptions" target="_blank">Errors and Exceptions</a> </li>
<li><a href="https://intranet.hbtn.io/rltoken/OTYmJ8UpJotqIVyrVgSL4A" title="Learn to Program 11 Static &amp; Exception Handling" target="_blank">Learn to Program 11 Static &amp; Exception Handling</a> (<em>starting at minute 7</em>)</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://intranet.hbtn.io/rltoken/TnecOG_n964IZ9aQvErdtQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome </li>
<li>What’s the difference between errors and exceptions</li>
<li>What are exceptions and how to use them</li>
<li>When do we need to use exceptions</li>
<li>How to correctly handle an exception</li>
<li>What’s the purpose of catching exceptions</li>
<li>How to raise a builtin exception</li>
<li>When do we need to implement a clean-up action after an exception</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </div>
</div>


      

      

        
          <h2 class="gap">Tasks</h2>

    <div data-role="task19418" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19418">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Safe list printing
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19418" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints <code>x</code> elements of a list.</p>

<ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>0-safe_print_list.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19418" data-batch-id="385" data-toggle="modal" data-target="#task-19418-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19418-users-done-modal" data-task-id="19418" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. Safe list printing"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19418" data-toggle="modal" data-target="#task-test-correction-19418-correction-modal" id="task-num-0-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19418-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "0. Safe list printing"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19418" data-last-request-id="9461193">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19418">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/b84bbe84a0f5350721fe22ba9667f3cbf71cdd1e">Click here</a></li><li><b>ID: </b><code>b84bbe84a0f5350721fe22ba9667f3cbf71cdd1e</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>I initialization</em></li><li><b>Date: </b><span>2023-06-07 09:33:37 -0700</span></li></ul></div><div class="check-inline requirement success" id="131265" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131264" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131266" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131267" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline requirement success" id="131268" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline requirement success" id="131269" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline requirement success" id="131276" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div><div class="check-inline code success" id="131274" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 7</div><div class="check-inline code success" id="131273" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 8</div><div class="check-inline code success" id="131270" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 9</div><div class="check-inline code success" id="131271" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 10</div><div class="check-inline code success" id="131272" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 11</div><div class="check-inline code success" id="131275" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 12</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19418">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19418">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19418-score-info-score">11</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19419" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19419">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Safe printing of an integers list
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19419" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints an integer with <code>"{:d}".format()</code>.</p>

<ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>1-safe_print_integer.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19419" data-batch-id="385" data-toggle="modal" data-target="#task-19419-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19419-users-done-modal" data-task-id="19419" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. Safe printing of an integers list"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19419" data-toggle="modal" data-target="#task-test-correction-19419-correction-modal" id="task-num-1-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19419-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "1. Safe printing of an integers list"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19419" data-last-request-id="9461317">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19419">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/11ad1ae30e67e49a524cf378bf119aee3a7a3319">Click here</a></li><li><b>ID: </b><code>11ad1ae30e67e49a524cf378bf119aee3a7a3319</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Except for lists</em></li><li><b>Date: </b><span>2023-06-07 09:43:00 -0700</span></li></ul></div><div class="check-inline requirement success" id="131277" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131278" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131279" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131280" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline requirement success" id="131281" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline requirement success" id="131282" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline requirement success" id="131291" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div><div class="check-inline code success" id="131289" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 7</div><div class="check-inline code success" id="131284" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 8</div><div class="check-inline code success" id="131285" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 9</div><div class="check-inline code success" id="131288" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 10</div><div class="check-inline code success" id="131286" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 11</div><div class="check-inline code success" id="131290" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 12</div><div class="check-inline code success" id="131283" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 13</div><div class="check-inline code success" id="131287" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 14</div><div class="check-inline code success" id="131292" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 15</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19419">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19419">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19419-score-info-score">14</span>/14
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19420" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19420">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Print and count integers
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19420" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p>

<ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code> - if it’s the case, an exception is expected to occur</li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in &lt;module&gt;
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>2-safe_print_list_integers.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19420" data-batch-id="385" data-toggle="modal" data-target="#task-19420-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19420-users-done-modal" data-task-id="19420" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. Print and count integers"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19420" data-toggle="modal" data-target="#task-test-correction-19420-correction-modal" id="task-num-2-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19420-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "2. Print and count integers"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19420" data-last-request-id="9462331">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19420">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/a9aa392d7cb674ddbba29f62056887708113acdd">Click here</a></li><li><b>ID: </b><code>a9aa392d7cb674ddbba29f62056887708113acdd</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Safe Print List</em></li><li><b>Date: </b><span>2023-06-07 10:40:36 -0700</span></li></ul></div><div class="check-inline requirement success" id="131293" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131294" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131295" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131296" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline requirement success" id="131297" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline requirement success" id="131298" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline requirement success" id="131307" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div><div class="check-inline code success" id="131301" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 7</div><div class="check-inline code success" id="131299" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 8</div><div class="check-inline code success" id="131303" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 9</div><div class="check-inline code success" id="131302" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 10</div><div class="check-inline code success" id="131304" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 11</div><div class="check-inline code success" id="131306" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 12</div><div class="check-inline code success" id="131305" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 13</div><div class="check-inline code success" id="131300" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 14</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19420">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19420">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19420-score-info-score">13</span>/13
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19421" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19421">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Integers division with debug
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19421" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that divides 2 integers and prints the result.</p>

<ul>
<li>Prototype: <code>def safe_print_division(a, b):</code></li>
<li>You can assume that <code>a</code> and <code>b</code> are integers</li>
<li>The result of the division should print on the <code>finally:</code> section preceded by <code>Inside result:</code></li>
<li>Returns the value of the division, otherwise: <code>None</code></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You have to use <code>"{}".format()</code> to print the result</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>3-safe_print_division.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19421" data-batch-id="385" data-toggle="modal" data-target="#task-19421-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19421-users-done-modal" data-task-id="19421" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "3. Integers division with debug"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19421" data-toggle="modal" data-target="#task-test-correction-19421-correction-modal" id="task-num-3-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19421-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "3. Integers division with debug"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19421" data-last-request-id="9462402">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19421">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/d4b5aea294af0f699e952b325348224f5b39cf01">Click here</a></li><li><b>ID: </b><code>d4b5aea294af0f699e952b325348224f5b39cf01</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Safe Print Div</em></li><li><b>Date: </b><span>2023-06-07 10:44:36 -0700</span></li></ul></div><div class="check-inline requirement success" id="131308" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131309" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131310" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131311" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline requirement success" id="131312" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline requirement success" id="131318" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline code success" id="131315" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div><div class="check-inline code success" id="131314" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 7</div><div class="check-inline code success" id="131317" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 8</div><div class="check-inline code success" id="131313" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 9</div><div class="check-inline code success" id="131316" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 10</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19421">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19421">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19421-score-info-score">10</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19422" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19422">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Divide a list
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19422" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that divides element by element 2 lists.</p>

<ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can’t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:

<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can’t be done (<code>/0</code>):

<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short

<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>4-list_division.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19422" data-batch-id="385" data-toggle="modal" data-target="#task-19422-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19422-users-done-modal" data-task-id="19422" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "4. Divide a list"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19422" data-toggle="modal" data-target="#task-test-correction-19422-correction-modal" id="task-num-4-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19422-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "4. Divide a list"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19422" data-last-request-id="9463385">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19422">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/427618b08cf4faf5a2ca635262db1f82902af42e">Click here</a></li><li><b>ID: </b><code>427618b08cf4faf5a2ca635262db1f82902af42e</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Error Output Fix</em></li><li><b>Date: </b><span>2023-06-07 12:01:11 -0700</span></li></ul></div><div class="check-inline requirement success" id="131319" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131320" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131321" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131322" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline requirement success" id="131331" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline code success" id="131323" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline code success" id="131334" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div><div class="check-inline code success" id="131324" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 7</div><div class="check-inline code success" id="131333" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 8</div><div class="check-inline code success" id="131329" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 9</div><div class="check-inline code success" id="131327" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 10</div><div class="check-inline code success" id="131328" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 11</div><div class="check-inline code success" id="131326" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 12</div><div class="check-inline code success" id="131332" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 13</div><div class="check-inline code success" id="131325" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 14</div><div class="check-inline code success" id="131330" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 15</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19422">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19422">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19422-score-info-score">16</span>/16
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19423" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19423">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Raise exception
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19423" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that raises a type exception.</p>

<ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/$ ./5-main.py
Exception raised
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>5-raise_exception.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19423" data-batch-id="385" data-toggle="modal" data-target="#task-19423-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19423-users-done-modal" data-task-id="19423" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "5. Raise exception"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19423" data-toggle="modal" data-target="#task-test-correction-19423-correction-modal" id="task-num-5-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19423-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "5. Raise exception"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19423" data-last-request-id="9463088">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19423">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/75eb7d4eaaf98c61ed152964192e4e6c4148a346">Click here</a></li><li><b>ID: </b><code>75eb7d4eaaf98c61ed152964192e4e6c4148a346</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Raise Exception</em></li><li><b>Date: </b><span>2023-06-07 11:31:48 -0700</span></li></ul></div><div class="check-inline requirement success" id="131335" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131336" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131337" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131339" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline code success" id="131338" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19423">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19423">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19423-score-info-score">11</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19424" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-19424">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Raise a message
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19424" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that raises a name exception with a message.</p>

<ul>
<li>Prototype: <code>def raise_exception_msg(message=""):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/$ ./6-main.py
C is fun
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>6-raise_exception_msg.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19424" data-batch-id="385" data-toggle="modal" data-target="#task-19424-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19424-users-done-modal" data-task-id="19424" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "6. Raise a message"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19424" data-toggle="modal" data-target="#task-test-correction-19424-correction-modal" id="task-num-6-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19424-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "6. Raise a message"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info"><strong>Congratulations!</strong> All tests passed successfully!<br>You are ready for your next mission!</div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19424" data-last-request-id="9463112">Start a new test</button>
                        <button class="btn btn-default close-modal" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error" style="display: none;"></div>
                        <div class="info" style="display: none;"></div>


                            <div class="cta-button" data-task-id="19424">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result" style="display: block;"><hr><h4>Result:</h4><div class="well"><h5>Commit used:</h5><ul><li><b>URL: </b><a target="_blank" href="https://github.com/Patricio-Benglian/holbertonschool-higher_level_programming/tree/65c944796ddf748f2d9434fff55993ebc965533a">Click here</a></li><li><b>ID: </b><code>65c944796ddf748f2d9434fff55993ebc965533a</code></li><li><b>Author: </b><span>Patricio-Benglian</span></li><li><b>Subject: </b><em>Raise Exception with Message</em></li><li><b>Date: </b><span>2023-06-07 11:34:23 -0700</span></li></ul></div><div class="check-inline requirement success" id="131340" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 0</div><div class="check-inline requirement success" id="131341" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 1</div><div class="check-inline requirement success" id="131342" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 2</div><div class="check-inline requirement success" id="131346" title="Requirement - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 3</div><div class="check-inline code success" id="131345" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 4</div><div class="check-inline code success" id="131344" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 5</div><div class="check-inline code success" id="131343" title="Correct output of your code - success"><i class="fa fa-check-circle" aria-hidden="true"></i>Check 6</div></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help" style="display: block;">
    <button data-task-id="19424">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19424">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-success">
              <span id="task-19424-score-info-score">9</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19425" data-position="100" id="task-num-7">
      <div class="panel panel-default task-card " id="task-19425">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Safe integer print with error message
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19425" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 0%;">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0.00%</span> (<span class="task_progress_value">Checks completed: 0.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints an integer.</p>

<ul>
<li>Prototype: <code>def safe_print_integer_err(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code> and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print as integer</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
guillaume@ubuntu:~/$ ./100-main.py 2&gt; /dev/null
89
-89
School is not an integer
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>100-safe_print_integer_err.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19425" data-batch-id="385" data-toggle="modal" data-target="#task-19425-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19425-users-done-modal" data-task-id="19425" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "7. Safe integer print with error message"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19425" data-toggle="modal" data-target="#task-test-correction-19425-correction-modal" id="task-num-7-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19425-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "7. Safe integer print with error message"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19425">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="19425">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="19425">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19425">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19425-score-info-score">0</span>/14
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19426" data-position="101" id="task-num-8">
      <div class="panel panel-default task-card " id="task-19426">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Safe function
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19426" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 0%;">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0.00%</span> (<span class="task_progress_value">Checks completed: 0.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that executes a function safely.  </p>

<ul>
<li>Prototype: <code>def safe_function(fct, *args):</code></li>
<li>You can assume <code>fct</code> will be always a pointer to a function</li>
<li>Returns the result of the function,</li>
<li>Otherwise, returns <code>None</code> if something happens during the function and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i &lt; len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

guillaume@ubuntu:~/$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
guillaume@ubuntu:~/$ ./101-main.py 2&gt; /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>101-safe_function.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19426" data-batch-id="385" data-toggle="modal" data-target="#task-19426-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19426-users-done-modal" data-task-id="19426" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "8. Safe function"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19426" data-toggle="modal" data-target="#task-test-correction-19426-correction-modal" id="task-num-8-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19426-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "8. Safe function"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19426">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="19426">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="19426">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19426">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19426-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19427" data-position="102" id="task-num-9">
      <div class="panel panel-default task-card " id="task-19427">
  <span id="user_id" data-id="6305"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. ByteCode -&gt; Python #4
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6305"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="19427" data-correction-id="481631">
        <div class="task_progress_bar" style="width: 0%;">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0.00%</span> (<span class="task_progress_value">Checks completed: 0.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        &gt;&gt;   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (&gt;)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     &gt;&gt;   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        &gt;&gt;   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     &gt;&gt;   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        &gt;&gt;  102 POP_BLOCK

 13     &gt;&gt;  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
</code></pre>

<ul>
<li>Tip: <a href="https://intranet.hbtn.io/rltoken/YPwcTnDHi4BeeC6tHmVVng" title="Python bytecode" target="_blank">Python bytecode</a></li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-exceptions</code></li>
            <li>File: <code>102-magic_calculation.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19427" data-batch-id="385" data-toggle="modal" data-target="#task-19427-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19427-users-done-modal" data-task-id="19427" data-batch-id="385">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "9. ByteCode -&gt; Python #4"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="19427" data-toggle="modal" data-target="#task-test-correction-19427-correction-modal" id="task-num-9-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19427-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "9. ByteCode -&gt; Python #4"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19427">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="19427">&lt; <a href="https://intranet.hbtn.io/projects/2122#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2021" target="_blank">
                            <img src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/pride-hbtn-87864ede8d6b828eed9247834f913523e2a5c16263562e807d5acccb44ed30ad.png">
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="19427">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19427">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19427-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>



          <div class="gap">
  <div data-react-class="projects/ProjectReview" data-react-props="{&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/481631/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/481631/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;sLI0DajVOyjd9AcUakHjW-q35FusbGxb3g14fn6hvny7A37ND4HyZ4g2c9fNxXh4TtKCCrKeTIvb6lKEroBfVw&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;The next project will be available on Monday, Jun 12th.&quot;,&quot;uri&quot;:null},&quot;fetchURI&quot;:&quot;/projects/2122/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:false,&quot;completion&quot;:{&quot;count&quot;:7,&quot;is_completed&quot;:true,&quot;percentage&quot;:100.0},&quot;inability_to_execute_reason&quot;:&quot;done&quot;},&quot;tasks&quot;:[{&quot;id&quot;:19418,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:11,&quot;score&quot;:11.0}},{&quot;id&quot;:19419,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:14,&quot;score&quot;:14.0}},{&quot;id&quot;:19420,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:13,&quot;score&quot;:13.0}},{&quot;id&quot;:19421,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:10,&quot;score&quot;:10.0}},{&quot;id&quot;:19422,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:16,&quot;score&quot;:16.0}},{&quot;id&quot;:19423,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:11,&quot;score&quot;:11.0}},{&quot;id&quot;:19424,&quot;progress_score&quot;:{&quot;progress&quot;:1.0,&quot;score&quot;:1.0},&quot;score_info&quot;:{&quot;passed&quot;:true,&quot;points&quot;:9,&quot;score&quot;:9.0}},{&quot;id&quot;:19425,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:14,&quot;score&quot;:0}},{&quot;id&quot;:19426,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}},{&quot;id&quot;:19427,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:100.0,&quot;score&quot;:{&quot;mandatory&quot;:100.0,&quot;optional&quot;:0.0}},&quot;can_skip&quot;:false,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:100.0,&quot;id&quot;:2122,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Exceptions&quot;,&quot;score&quot;:{&quot;mandatory&quot;:100.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:3},&quot;skipURI&quot;:&quot;/corrections/481631/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Score</h3></div><div class="panel-body"><div class="align-items-center d-flex gap-5"><div class="pathway" style="padding: 10px 30px 40px;"><div class="project-circle " style="border-radius: 100%; box-shadow: rgb(229, 230, 230) 10px 20px 10px; height: 125px; margin: auto; padding: 5px; width: 125px;"><div data-test-id="CircularProgressbarWithChildren"><div style="position: relative; width: 100%; height: 100%;"><svg class="CircularProgressbar " viewBox="0 0 100 100" data-test-id="CircularProgressbar" style="height: 115px; vertical-align: middle; width: 115px;"><path class="CircularProgressbar-trail" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 0px;"></path><path class="CircularProgressbar-path" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 0px;"></path></svg><div data-test-id="CircularProgressbarWithChildren__children" style="position: absolute; width: 100%; height: 100%; margin-top: -100%; display: flex; flex-direction: column; justify-content: center; align-items: center;"><div style="height: 100%; position: absolute; transform: rotate(0turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div style="height: 100%; position: absolute; transform: rotate(0.333333turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div style="height: 100%; position: absolute; transform: rotate(0.666667turn);"><div class="circular-progress-bar-radial-separator" style="height: 4%; width: 8px;"></div></div><div class="position-relative"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Python - Exceptions"><div class="align-items-center d-flex justify-content-center project-circle-body active" style="border-radius: 100%; height: 100px; width: 100px;"><img alt="Project badge" src="./Project_ Python - Exceptions _ Holberton Montevideo, Uruguay Intranet_files/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png" width="60%"></div></span><div class="p-1 position-absolute project-circle-score text-center" style="border-radius: 10px; width: 100px;"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Score of Mandatory Tasks"><span class="d-block">100%</span></span></div></div></div></div></div></div></div><div style="flex-basis: 100%;"><p class="mb-2 text-primary"><span>Congratulations! You made it!</span></p><div><p>The next project will be available on Monday, Jun 12th.</p></div><div class="d-flex flex-wrap gap-3 justify-content-between mt-4"><div class="btn-group"><a class="btn btn-primary" href="https://intranet.hbtn.io/"><i aria-hidden="true" class="fa fa-home"></i><span class="ml-2">Go to home</span></a></div><div></div></div></div></div></div></div></div>
</div>



          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true,&quot;container&quot;:{&quot;container_id&quot;:&quot;68a95bf51f0637daa32bf6cb8d8249968b4e17e51d891b478efa6a0869aee45e&quot;,&quot;id&quot;:28258,&quot;restart_uri&quot;:&quot;/user_containers/28258/restart.json&quot;,&quot;status&quot;:&quot;running&quot;,&quot;uri&quot;:&quot;/user_containers/28258.json&quot;,&quot;wake_uri&quot;:&quot;/user_containers/28258/wake.json&quot;,&quot;webterm_uri&quot;:&quot;/user_containers/28258/webterm&quot;,&quot;host&quot;:&quot;68a95bf51f06.e9735203.hbtn-cod.io&quot;,&quot;password&quot;:&quot;c7ba14db4d30d13624e3&quot;,&quot;ports&quot;:{&quot;3306&quot;:53738,&quot;5000&quot;:53736,&quot;5001&quot;:53735,&quot;8000&quot;:53734,&quot;8080&quot;:53733,&quot;22&quot;:53742,&quot;3000&quot;:53739,&quot;4000&quot;:53737,&quot;443&quot;:53740,&quot;80&quot;:53741}}}],&quot;containersLimit&quot;:5,&quot;csrfToken&quot;:&quot;BLspswtBYINnbMpeu_vaBMqsb7wOSNUXhhJDSDQwbt8PCmNzrBWpzDKuvp0cf0EnbskJ7RC69ceD9Wmy5BGP9A&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"><div><div class="d-flex gap-4 sandboxes-filters"><a class="btn btn-outline-primary"><i aria-hidden="true" class="fa fa-filter"></i><span class="ml-2">Running only</span></a><div class="align-items-center d-flex" style="position: relative; width: 100%;"><input class="form-control" placeholder="Search for an image ..." type="search" value=""></div></div><div class="mt-3"><h3>1 image<small class="ml-2">(1/5 Sandboxes spawned)</small></h3></div><div class="mt-3"><div class="panel panel-default"><div class="panel-body border-left-success" style="border-left: 6px solid;"><div class="align-items-center d-flex flex-wrap justify-content-between"><div><h3 class="mt-0"><i aria-hidden="true" class="fa fa-terminal text-success"></i><span class="ml-2">Ubuntu 20.04</span></h3><div class="mt-2 text-muted"><p>Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations</p>
</div></div><div class="d-flex flex-wrap gap-5"><div class="align-items-center d-flex gap-3"><div><span data-container="body" data-html="false" data-placement="top" data-toggle="tooltip" title="" data-original-title="Copy SSH command"><span role="button"><button class="btn btn-default">SSH</button></span></span></div><div><span data-container="body" data-html="false" data-placement="top" data-toggle="tooltip" title="" data-original-title="Copy SFTP command"><span role="button"><button class="btn btn-default">SFTP</button></span></span></div><a class="btn btn-webterm" href="https://intranet.hbtn.io/user_containers/28258/webterm" rel="noreferrer" target="_blank"><i aria-hidden="true" class="fa fa-terminal"></i><span class="ml-2">Webterm</span></a></div><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Restart your Sandbox"><a class="btn btn-warning "><i aria-hidden="true" class="fa fa-power-off"></i><span class="ml-2">Restart</span></a></span><a class="btn btn-danger"><i aria-hidden="true" class="fa fa-trash"></i><span class="ml-2">Destroy</span></a></div></div><div class="d-flex flex-wrap gap-5 mt-3"><div class="p-4" style="flex-shrink: 0;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa fa-user text-info"></i><span class="ml-2">Credentials</span></h4><div class="d-flex gap-2"><strong>Host</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>68a95bf51f06.e9735203.hbtn-cod.io</small></span></span></div><div class="d-flex gap-2"><strong>Username</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>68a95bf51f06</small></span></span></div><div class="d-flex gap-2"><strong>Password</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>c7ba14db4d30d13624e3</small></span></span></div></div></div><div class="p-4" style="flex: 1 1 40%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa fa-globe text-info"></i><span class="ml-2">Web access</span></h4><div class="align-items-center d-flex flex-wrap gap-2"><a class="btn btn-outline-primary" href="https://68a95bf51f06.e9735203.hbtn-cod.io/" rel="noreferrer" target="_blank">HTTPS</a><a class="btn btn-outline-primary" href="http://68a95bf51f06.e9735203.hbtn-cod.io/" rel="noreferrer" target="_blank">HTTP</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:3000/" rel="noreferrer" target="_blank">3000</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:4000/" rel="noreferrer" target="_blank">4000</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:5000/" rel="noreferrer" target="_blank">5000</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:5001/" rel="noreferrer" target="_blank">5001</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:8000/" rel="noreferrer" target="_blank">8000</a><a class="btn btn-default" href="http://68a95bf51f06.e9735203.hbtn-cod.io:8080/" rel="noreferrer" target="_blank">8080</a></div></div></div><div class="p-4" style="flex: 1 1 35%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa fa-map-signs text-info"></i><span class="ml-2">Port mapping</span></h4><div class="align-items-center d-flex flex-wrap"><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>SSH</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53742</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTP</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53741</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTPS</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53740</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>3000</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53739</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>MySQL</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53738</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>4000</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53737</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5000</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53736</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5001</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53735</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8000</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53734</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8080</strong><i aria-hidden="true" class="fa fa-long-arrow-right"></i><span>53733</span></div></div></div></div></div></div></div></div></div></div></div></div></div></div>

        <div>
          <a data-toggle="tooltip" title="" href="https://intranet.hbtn.io/projects/2121" data-original-title="Python - More Data Structures: Set, Dictionary">Previous project</a>
        </div>
  </div>
</div>


      </article>

      <div class="copyright">Copyright © 2023 Holberton Inc, All rights reserved.</div>
    </main>

      <button class="btn btn-primary" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
  <i aria-hidden="true" class="fa fa-search "></i>
  <i aria-hidden="true" class="fa fa-window-minimize "></i>
</button>

      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar" type="text" name="hbtn-search-bar" placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>



      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>&gt; This is a quote.
&gt; It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '6305'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>



      <input id="checker_pride_assets" type="hidden" value="[[&quot;prideflag-gay.png&quot;,&quot;The Gay Pride Flag&quot;,[&quot;THE MEANING: According to Robert Deam Tobin, PhD, who teaches courses in gay and lesbian studies and queer theory at Clark University, the gay pride flag \&quot;was and is a cheerful, upbeat, optimistic, and instantly identifiable symbol of the LGBTQ+ community—and has caught on throughout the world, in big cities and little ones.\&quot; He also notes: “The colors were chosen from the rainbow, a symbol of hope ever since Noah’s flood.&quot;,&quot;THE HISTORY: \&quot;Gilbert Baker created the rainbow flag in San Francisco in 1978, as the gay community was flourishing and beginning to fight for its rights,\&quot; explains Tobin, noting that the Stonewall Riots took place in 1969 and the first gay pride parade took place in 1970.&quot;,&quot;Fun fact: Tobin says the flag was originally supposed to have eight colors instead of the six we see today, but Gilbert wound up having to axe both turquoise and pink to make the design simple enough for mass production.&quot;]],[&quot;prideflag-updated.png&quot;,&quot;The Updated Gay Pride Flag&quot;,[&quot;THE MEANING: This flag, Tobin says, was created recently as a response \&quot;to new developments in the LGBTQ+ community, particularly to be inclusive in terms of race and trans issues.\&quot;&quot;,&quot;THE HISTORY: The updated flag was developed by Daniel Quasar in 2018. \&quot;In 2017, the so-called &#39;Philadelphia flag&#39; had incorporated a black and a brown stripe on top of the six colors of the rainbow flag,\&quot; Tobin explains. \&quot;Quasar&#39;s version moved the black and the brown to the side as part of a triangle that also included the colors of the trans flag intersecting with the now-traditional rainbow flag.\&quot;&quot;]],[&quot;prideflag-lesbian.png&quot;,&quot;The Lesbian Pride Flag&quot;,[&quot;THE MEANING: This is the newest version of the lesbian pride flag, and Tobin explains it is \&quot;trying to signal toward diversity with the orange line suggesting gender nonconformity.\&quot;&quot;,&quot;THE HISTORY: There&#39;s a lot of history when it comes to lesbian pride flags, so buckle up, people: \&quot;There are actually a variety of lesbian flags,\&quot; says Tobin. \&quot;In addition to the one shown here, there is also a purple one created in 1999—ironically, or problematically, by a man.\&quot;&quot;,&quot;In addition to being designed by a dude, Tobin explains that particular flag was problematic because it featured \&quot;a double-edged axe, known as a labrys, set in an inverted triangle\&quot; that looked a lot like \&quot;the black triangle used to identify some lesbians in Nazi concentration camps.\&quot; An updated one came in 2010 featuring shades of pink and a lipstick stain as an ode to \&quot;lipstick lesbians,\&quot; but this new one is here to symbolize diversity.&quot;]],[&quot;prideflag-transgender.png&quot;,&quot;The Transgender Pride Flag&quot;,[&quot;THE MEANING: This is the transgender pride flag and it purposely plays with the traditional colors for baby boys and girls.&quot;,&quot;THE HISTORY: \&quot;Monica Helms created the transgender pride flag in 1999,\&quot; says Tobin. \&quot;In my work on local gay history, I&#39;ve noticed that the 1990s is when many groups start adding the &#39;T&#39; for transgender to their names. This flag is becoming quite well recognized, in part because the trans community has had to fight many battles: ensuring medical access, fighting discrimination in the military and elsewhere, providing resources for trans youth, taking on hostile state laws, and fighting discriminatory ballot measures.\&quot;&quot;]],[&quot;prideflag-intersex.png&quot;,&quot;The Intersex Pride Flag&quot;,[&quot;THE MEANING: While the transgender pride flag plays with traditional colors, Tobin notes that \&quot;the intersex pride flag works with colors that have not been traditionally gendered, like yellow.\&quot; As for the circle, Tobin says that \&quot;represents wholeness.\&quot;&quot;,&quot;THE HISTORY: \&quot;The intersex pride flag was created in Australia in 2013,\&quot; says Tobin. \&quot;The flag has undoubtedly helped unify the intersex community, which has had to bond together to fight medical and political battles, notably making sure that physicians didn&#39;t undertake corrective surgery on people born intersex before those people were able to give consent.\&quot;&quot;]],[&quot;prideflag-bisexual.png&quot;,&quot;The Bisexual Pride Flag&quot;,[&quot;THE MEANING: According to Tobin, the idea behind the bisexual pride flag is \&quot;the pink represents same-sex attraction, the blue represents heterosexual attraction, and the two colors fade imperceptibly into each other to create purple.\&quot;&quot;,&quot;THE HISTORY: \&quot;Michael Page designed the bisexual pride flag in 1998,\&quot; says Tobin. \&quot;It&#39;s interesting that, in general, at the end of the 1990s, you see the addition of the lesbian, trans, and bisexual flags, after the rainbow flag had been around for two decades. It&#39;s as though the 1990s was a moment of understanding the need for communities to break out and create their own identities.\&quot;&quot;]],[&quot;prideflag-pansexual.png&quot;,&quot;The Pansexual Pride Flag&quot;,[&quot;THE MEANING: See the pink and blue parts of the flag? Okay, well, Tobin says those parts represent traditional genders, \&quot;while the yellow represents nonbinary people.\&quot; He also notes it&#39;s that yellow part that distinguishes this flag from the bisexual one.&quot;,&quot;THE HISTORY: \&quot;The pansexual pride flag has been around since the 2010s,\&quot; says Tobin. While there isn&#39;t much intel out there on who created it, most sources agree it was created on the internet.&quot;]],[&quot;prideflag-asexual.png&quot;,&quot;The Asexual Pride Flag&quot;,[&quot;THE MEANING: This flag may be the asexual pride flag, but it&#39;s not strictly for asexuals. \&quot;Its colors are designed to include graysexuals, who operate in the &#39;gray space&#39; between sexuality and asexuality, as well as demisexuals, who only feel sexual attraction under certain circumstances,\&quot; explains Tobin.&quot;,&quot;THE HISTORY: According to The Asexual Agenda, the flag came to be in July of 2010 when the Asexual Visibility and Education Network (AVEN) came together to push the community into deciding upon a flag. After three stages of polls, the asexual flag we have today was announced.&quot;]],[&quot;prideflag-nonbinary.png&quot;,&quot;The Nonbinary Pride Flag&quot;,[&quot;THE MEANING: According to Tobin, this particular flag is meant to \&quot;represent people outside the traditional gender binary, people with multiple genders, people with mixed genders, and people with no genders.\&quot;&quot;,&quot;THE HISTORY: Tobin says the nonbinary flag we see today was first created by Kye Rowan in 2014.&quot;]],[&quot;prideflag-genderfluid.png&quot;,&quot;The Genderfluid Pride Flag&quot;,[&quot;THE MEANING: \&quot;This flag goes from pink, representing femininity, to blue, representing masculinity, and tries to cover everything in between,\&quot; notes Tobin.&quot;,&quot;THE HISTORY: According to Out Right International, this flag was created by JJ Poole in 2012.&quot;]],[&quot;prideflag-genderqueer.png&quot;,&quot;The Genderqueer Pride Flag&quot;,[&quot;THE MEANING: The colors of this flag, says Tobin, all represent \&quot;androgyny, agender, and nonbinary identities.\&quot;&quot;,&quot;THE HISTORY: The genderqueer pride flag was created by Marilyn Roxie in 2011, says Tobin.&quot;]],[&quot;prideflag-agender.png&quot;,&quot;The Agender Pride Flag&quot;,[&quot;THE MEANING: According to Tobin, \&quot;This flag chooses colors that have not been traditionally gendered.\&quot; Specifically, Out Right International notes \&quot;the black and white stripes represent an absence of gender, the gray represents semi-genderlessness, and the central green stripe represents nonbinary genders.\&quot;&quot;,&quot;THE HISTORY: According to Out Right International, the agender pride flag was created by Salem X in 2014.&quot;]]]">

      


  

</body></html>