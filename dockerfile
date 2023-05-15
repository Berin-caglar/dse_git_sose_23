FROM alpine:3.4
RUN apk add --no-cache bash
CMD while date; do sleep 1; done
