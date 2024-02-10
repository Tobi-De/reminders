# Stage 1: General enviroment
FROM python:3.12-slim-bookworm AS python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$VENV_PATH/bin:$PATH"
ARG S6_OVERLAY_VERSION=3.1.6.2

# Stage 2: Install dependencies & build static files
FROM python-base as builder-base

# Install dependencies
WORKDIR $PYSETUP_PATH
COPY ./requirements.txt ./
RUN python -m venv $VENV_PATH && \
    pip install -r requirements.txt

# s6 install
RUN apt-get update && apt-get install -y xz-utils
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp

# Build static files
COPY . /app
WORKDIR /app
RUN python manage.py collectstatic --no-input

# Stage 3: Run service
FROM python-base as production

# s6 install
COPY --from=builder-base /usr/bin/xz /usr/bin/xz
COPY --from=builder-base /tmp/s6-overlay-noarch.tar.xz /tmp/s6-overlay-noarch.tar.xz
COPY --from=builder-base /tmp/s6-overlay-x86_64.tar.xz /tmp/s6-overlay-x86_64.tar.xz
RUN tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz
RUN tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz

# copy config files, s6 + litestream
COPY deploy/etc  /etc

# The kill grace time is set to zero because our app handles shutdown through SIGTERM.
ENV S6_KILL_GRACETIME=0

# Sync disks is enabled so that data is properly flushed.
ENV S6_SYNC_DISKS=1

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY --from=builder-base /app/staticfiles /app/staticfiles
COPY . /app

# WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["/init"]
