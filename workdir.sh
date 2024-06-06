# Create project directory.
mkdir custom-fluentd
cd custom-fluentd

# Download default fluent.conf and entrypoint.sh. This file will be copied to the new image.
# VERSION is v1.7 like fluentd version and OS is alpine or debian.
# Full example is https://raw.githubusercontent.com/fluent/fluentd-docker-image/master/v1.10/debian/fluent.conf

curl https://raw.githubusercontent.com/fluent/fluentd-docker-image/master/VERSION/OS/fluent.conf > fluent.conf

curl https://raw.githubusercontent.com/fluent/fluentd-docker-image/master/VERSION/OS/entrypoint.sh > entrypoint.sh
chmod +x entrypoint.sh

# Create plugins directory. plugins scripts put here will be copied to the new image.
mkdir plugins

curl https://raw.githubusercontent.com/fluent/fluentd-docker-image/master/Dockerfile.sample > Dockerfile
