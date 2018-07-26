FROM alephdata/memorious

RUN pip install --upgrade pandas unicodecsv xlrd attrs

COPY . /opensanctions
RUN pip install -e /opensanctions

ENV MEMORIOUS_CONFIG_PATH=/opensanctions/opensanctions/config \
    MEMORIOUS_EAGER=true

# Setup cron
RUN apt-get update && apt-get -y install -qq --force-yes cron

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

