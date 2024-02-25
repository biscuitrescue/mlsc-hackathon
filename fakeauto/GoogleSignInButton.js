import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
// import * as AuthSession from 'expo-auth-session';

const clientId = 'YOUR_CLIENT_ID'; // Replace with your actual Client ID
const discovery = {
  issuer: 'https://accounts.google.com',
  authorization_endpoint: 'https://accounts.google.com/o/oauth2/v2/auth',
  token_endpoint: 'https://accounts.google.com/o/oauth2/v2/token',
  userinfo_endpoint: 'https://openidconnect.googleapis.com/v1/userinfo',
};

const scopes = [
  'openid',
  'profile',
  'email', // Add more scopes as needed
];

const GoogleSignInButton = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [user, setUser] = useState(null);

  // const signInAsync = async () => {
  //   setIsLoading(true);
  //   try {
  //     const { authRequest, redirectUri } = AuthSession.makeAuthRequest({
  //       clientId,
  //       scopes,
  //       discovery,
  //       redirectUri: AuthSession.makeRedirectUri(),
  //     }, { useProxy: false }); // Disable proxy for security

  //     const result = await AuthSession.startAsync({ authRequest, redirectUri });
  //     if (result.type === 'success') {
  //       const { code } = result.params;
  //       const data = await AuthSession.fetchTokenAsync({
  //         method: 'POST',
  //         headers: {
  //           'Content-Type': 'application/x-www-form-urlencoded',
  //         },
  //         body: {
  //           grant_type: 'authorization_code',
  //           code,
  //           client_id: clientId,
  //           client_secret: YOUR_CLIENT_SECRET, // Replace with your Client Secret (if using)
  //           redirect_uri: redirectUri,
  //         },
  //       });

  //       const userInfoResponse = await fetch(discovery.userinfo_endpoint, {
  //         headers: { Authorization: `Bearer ${data.access_token}` },
  //       });
  //       const userInfo = await userInfoResponse.json();

  //       setUser(userInfo);
  //     }
  //   } catch (error) {
  //     console.error(error);
  //   } finally {
  //     setIsLoading(false);
  //   }
  // };

  // return (
  //   <View>
  //     {isLoading ? (
  //       <Text>Loading...</Text>
  //     ) : user ? (
  //       <Text>Welcome, {user.name}!</Text>
  //     ) : (
  //       <Button title="Sign in with Google" onPress={signInAsync} />
  //     )}
  //   </View>
  // );
};

export default GoogleSignInButton;
