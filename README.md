# django-docker-starter kit

This repository is a template for a [django]() and [django-rest-framework]() project. It has been containerized and composed with a [Postgres]() instance via the <i>Dockerfile</i> and <i>docker-compose.yml</i> in the root directory. The application comes pre-configured to connect to this instance when running as a container.

## Setup

### Enviroment

Copy the <i>/env/.sample.build.env</i> and <i>/env/.sample.runtime.env</i> into new <i>/env/build.env</i> and <i>/env/runtime.env</i> files respectively. Adjust the environment variables in these files to your specific situation. The <i>build.env</i> get injected into the <i>/scripts/docker/build-image.sh</i> shell script to configure the `docker build`. The <i>runtime.env</i> gets into injected into the <i>/scripts/run-server.sh</i>, <i>/scripts/docker/entrypoint.sh</i> and the <i>/scripts/docker/run-container.sh</i> shell scripts. These define the different starting points of the application.

### Shell Scripts

1. <b>/scripts/run-server.</b>

Arguments: Accepts an argument of either <b>dev</b> or <b>gunicorn</b>. If no argument is provided, the argument defaults to <b>gunicorn</b>. 

Description: Performs start up tasks, like collecting static files and migrating <b>django</b> models, and then starts up a local application server. If an argument of <b>dev</b> is provided, the script will invoke `python manage.py runserver` to start up a live development server. If an argument of <b>gunicorn</b> or no argument at all is provided, the script will deploy the application on the WSGI server, <b>gunicorn</b>

2. <b>/scripts/docker/build-image.sh</b>

Description: Initializes the <i>build.env</i> variables and uses them in calling `docker build`. Creates a <b>Docker</b> image of the application.

3. <b>/scripts/docker/run-container.sh</b>

Description: Initializes the <i>runtime.env</i> variables and feeds them into the container runtime. Starts up a container with the image name and tag created by the <i>build-image</i> script.

4. <b>/scripts/docker/entrypoint.sh</b>. 

Description: Tne entrypoint script that gets copied into the <b>Docker</b> image. Analogous to the <i>run-server</i> script in a containerized environment. Starts up the <b>Docker</b> container from inside of the container. 

5. <b>/scripts/util/env-vars.sh</b>

Arguments: The name of the enviroment file in the <i>/env/</i> directory you wanted loaded into the current shell session.

Description: Used to load in environment variables from a particular <i>.env</i> file.

6. <b>/scripts/util/sys-util.sh</b>

Description: Useful functions. Source this script, `source ./scripts/util/sys-util.sh`, to load these functions into your current shell session. <i>clean_docker</i> is a particularly useful function to cleaning up dangling <b>Docker</b> images, cleaning the cache and pruning orphaned volumes and networks. 