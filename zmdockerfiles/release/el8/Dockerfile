FROM rockylinux/rockylinux:8
MAINTAINER Andrew Bauer <zonexpertconsulting@outlook.com>

# Get the entrypoint script
ADD https://raw.githubusercontent.com/ZoneMinder/zmdockerfiles/master/utils/entrypoint.sh /usr/local/bin/

## Dependencies layer
RUN \
  # Enable PowerTools repository to reach all required dependencies
  dnf -y install 'dnf-command(config-manager)' && dnf config-manager --set-enabled powertools \
  # Enable the EPEL repo. The repo package is part of Rocky base so no need fetch it.
  && dnf -y install epel-release \
  # Fetch and enable the RPMFusion repo
  && dnf -y localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm \
  # Install dependencies
  && dnf -y install mariadb-server mod_ssl zip file \
  # Install support for hardware accelerator decoder devices
  && dnf -y install mesa-dri-drivers libva-intel-driver \
  # Clean up dnf cache
  && dnf clean all \
  # Make sure the entrypoint is executable
  && chmod 755 /usr/local/bin/entrypoint.sh

## ZoneMinder layer
RUN \
  # Install the latest *release* of zoneminder
  dnf -y install zoneminder \
  # Clean up dnf cache
  && dnf clean all \
  # Configure Apache
  && ln -sf /etc/zm/www/zoneminder.conf /etc/httpd/conf.d/ \
  && echo "ServerName localhost" > /etc/httpd/conf.d/servername.conf \
  && echo -e "# Redirect the webroot to /zm\nRedirectMatch permanent ^/$ /zm" > /etc/httpd/conf.d/redirect.conf

# Set our volumes before we do anything else
VOLUME /var/lib/zoneminder/events /var/lib/mysql /var/log/zoneminder

# Expose https port
EXPOSE 443

# This is run each time the container is started
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

################
# RUN EXAMPLES #
################

# ZoneMinder uses /dev/shm for shared memory and many users will need to increase 
# the size significantly at runtime like so:
#
# docker run -d -t -p 1080:443 \
#    --shm-size="512m" \
#    --name zoneminder \
#    zoneminder/zoneminder

# ZoneMinder checks the TZ environment variable at runtime to determine the timezone.
# If this variable is not set, then ZoneMinder will default to UTC.
# Alternaitvely, the timezone can be set manually like so:
#
# docker run -d -t -p 1080:443 \
#    -e TZ='America/Los_Angeles' \
#    --name zoneminder \
#    zoneminder/zoneminder

# ZoneMinder can write its data to folders outside the container using volumes.
#
# docker run -d -t -p 1080:443 \
#    -v /disk/zoneminder/events:/var/lib/zoneminder/events \
#    -v /disk/zoneminder/mysql:/var/lib/mysql \
#    -v /disk/zoneminder/logs:/var/log/zoneminder \
#    --name zoneminder \
#    zoneminder/zoneminder

# ZoneMinder can use an external database by setting the appropriate environment variables.
#
# docker run -d -t -p 1080:443 \
#    -e ZM_DB_USER='zmuser' \
#    -e ZM_DB_PASS='zmpassword' \
#    -e ZM_DB_NAME='zoneminder_database' \
#    -e ZM_DB_HOST='my_central_db_server' \
#    -v /disk/zoneminder/events:/var/lib/zoneminder/events \
#    -v /disk/zoneminder/logs:/var/log/zoneminder \
#    --name zoneminder \
#    zoneminder/zoneminder

# Here is an example using a Docker Secrets type password file:

# docker run -d -t -p 1080:443 \
#    -e ZM_DB_USER='zmuser' \
#    -e ZM_DB_PASS_FILE='/run/secure/zm_db_password' \
#    -e ZM_DB_NAME='zoneminder_database' \
#    -e ZM_DB_HOST='my_central_db_server' \
#    -v /disk/zoneminder/events:/var/lib/zoneminder/events \
#    -v /disk/zoneminder/logs:/var/log/zoneminder \
#    --name zoneminder \
#    zoneminder/zoneminder


# Here is an example using the options described above with the internal database:
#
# docker run -d -t -p 1080:443 \
#    -e TZ='America/Los_Angeles' \
#    -v /disk/zoneminder/events:/var/lib/zoneminder/events \
#    -v /disk/zoneminder/mysql:/var/lib/mysql \
#    -v /disk/zoneminder/logs:/var/log/zoneminder \
#    --shm-size="512m" \
#    --name zoneminder \
#    zoneminder/zoneminder

# Here is an example using the options described above with an external database:
#
# docker run -d -t -p 1080:443 \
#    -e TZ='America/Los_Angeles' \
#    -e ZM_DB_USER='zmuser' \
#    -e ZM_DB_PASS='zmpassword' \
#    -e ZM_DB_NAME='zoneminder_database' \
#    -e ZM_DB_HOST='my_central_db_server' \
#    -v /disk/zoneminder/events:/var/lib/zoneminder/events \
#    -v /disk/zoneminder/logs:/var/log/zoneminder \
#    --shm-size="512m" \
#    --name zoneminder \
#    zoneminder/zoneminder

