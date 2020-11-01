# flaskChat

This application is created using flask which is a microframework very easy to work with.
Steps to create this:
1. Create a bot in the telegram using <strong>BotFather</strong>. Then take the token provided by BotFather, this token is used for communicating with the telegram.
2. Then create a webhook which need to be a public API. one can use tools such as [ngrok](https://ngrok.com/) for tunneling which can be used for webhook.
   Webhooks are used for getting new messages for bots. Although one can check for updates on core API of telegram, but this would require calling the API at a frequent
   which can lead to spamming the telegram API. Thus the sophisticated approach is used the Webhooks.
3. Then we need to register the webhooks using on telegram endpoint so that telegram would know where to send the updates in case of new messages. we can use [setWebhook](https://core.telegram.org/bots/api#setwebhook)
   After this telegram will start to notify every time a new message is there.
4. After this we can use various methods that telegram supports for sending replies, making conversation, sending images etc. [learn more](https://core.telegram.org/bots/api#available-methods)
