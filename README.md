# Lambda Spot-Inst

Python Lambda script to start and stop the servers in spot-inst. You can set up and deploy as follows. In lambda console(or chalice/serverless), you need to setup [environment variables](#environment-variables).

[Spot-inst](https://spot.io/) is a SaaS based EC2 management solution that delivers cloud efficiences never before archieved. You can reduce EC2 cloud computing costs by 60% to 80%. It can be easily applied even in environments where are not using serverless or Kubernetics architectures.

## Set up

Start virtual envrionment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install package

```bash
pip3 install -r requirements.txt

## Or
pip3 install requests awscli
```

Setup variables and folder for deploy. (You can skip this step if you are using chalice or a serverless framework)

```bash
sh setup.sh

## Or
export OLDPWD=$(pwd)
mkdir package
pip install --target ./package requests
```

Server list in json file

```json
// ./server_list.json
// Specify your server information in your spot-inst
{
  {
    "dev": [
        {
            "name": "DEV_SERVER_NAME_1",
            "group_id": "sig-00000000",
            "instance_id": "ssi-aaaaaaa"
        },
    ],
    "prd": [
        {
            "name": "prd_SERVER_NAME_1",
            "group_id": "sig-11111111",
            "instance_id": "ssi-bbbbbbb"
        }
    ]
}
}
```

## Deploy

Make sure you have AWS configure&role and proceed with the steps below. If you want to change function name, you need to change script. Currently, there is no ability to accept variables dynamically.

```bash
## Create a ZIP archive of code
sh package.sh

## Make sure you have AWS configure and set up AWS role

## If it is first deploy
sh deploy.sh
## Or for update
sh update.sh
```

## Environment variables

You need to set up the following environment variable in the lambda console. If you are using chalice or serverless, you can specify variables according to the framework.

- environment variable: AUTH_TOKEN
- lambda timeout: 30s
- lambda test event: StartServer, StopServer

`StartServer.json`

```json
{
  "mode": 0,
  "server": "dev"
}
```

`StopServer.json`

```json
{
  "mode": 1,
  "server": "prd"
}
```
