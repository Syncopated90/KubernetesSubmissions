FROM alpine
WORKDIR /usr/src/app
COPY . .
RUN chmod +x randomURL.sh
RUN apk --no-cache add curl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin
CMD ["./randomURL.sh"]