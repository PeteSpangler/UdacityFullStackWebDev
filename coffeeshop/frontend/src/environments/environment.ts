/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

/*
Sources I got help from:

https://github.com/jungleBadger/udacity_coffee_shop/blob/master/troubleshooting/generate_token.md

https://github.com/jungleBadger/udacity_coffee_shop/blob/master/troubleshooting/update_postman.md
*/

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
      url: 'petespangler', // the auth0 domain prefix
      audience: 'localhost:5000', // the audience set for the auth0 app
      clientId: 'zcqHKh1q8H6YydYeJvQVxwo339X1ptoL', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
