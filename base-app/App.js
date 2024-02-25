// ios 411424392116-l0d85tr9g5uctbocjms6j6mvngl3pr5a.apps.googleusercontent.com
// android 411424392116-kbsqqf4agkdh280t19dl9qf9f22188ts.apps.googleusercontent.com

import React, { useState } from 'react';
import * as AuthSession from 'expo-auth-session';

import GoogleSignInButton from './GoogleSignInButton';

import {
  Image,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  Button,
} from "react-native";

import { StatusBar } from "expo-status-bar";

// const androidClientId = '411424392116-kbsqqf4agkdh280t19dl9qf9f22188ts.apps.googleusercontent.com';
// const iosClientId = '411424392116-l0d85tr9g5uctbocjms6j6mvngl3pr5a.apps.googleusercontent.com';

// import { useFonts } from 'expo-fonts';
import { useFonts, Inter_900Black } from '@expo-google-fonts/inter';


export default function App() {
  let [fontsLoaded, fontError] = useFonts({
    Inter_900Black,
  });
  
  

  return (
    <View style={styles.container}>
      <Image
        source={require("./assets/images/bg.jpeg")}
        style={styles.image}
        blurRadius={2}
      />
      <View style={styles.signInBox}>
        <Text style={styles.signInText}>Sign Up</Text>
        <View style={styles.inputContainer}>
        <TextInput
          style={styles.inputBox}
          placeholder="Full Name"
          placeholderTextColor="#7D8287"
        />
        <TextInput
          style={styles.inputBox}
          placeholder="Hostel"
          placeholderTextColor="#7D8287"
        />
          <TextInput
            style={styles.inputBox}
            placeholder="Thapar Mail Id"
            placeholderTextColor="#7D8287"
            secureTextEntry={true}
          />
        <TextInput
            style={styles.inputBox}
            placeholder="Username"
            placeholderTextColor="#7D8287"
          />
          <TextInput
            style={styles.inputBox}
            placeholder="Password"
            placeholderTextColor="#7D8287"
            secureTextEntry={true}
          />
        </View>
        <TouchableOpacity style={styles.submitButton} >
          <Text style={styles.submitText}>Submit</Text>
        </TouchableOpacity>
      </View>
      <StatusBar style="auto" />
      <GoogleSignInButton />

      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    position: "absolute",
    resizeMode: "cover",
    width: "100%",
    height: "100%",
    opacity: 1, // Add slight opacity for overlay effect
  },
  signInBox: {
    backgroundColor: "#7D8287",
    borderRadius: 10,
    padding: 20,
    marginTop: 20,
    width: "80%",
  },
  signInText: {
    textAlign: "center",
    color: "white",
    fontSize: 40,
    fontWeight: "bold",
    marginBottom: 20,
    fontFamily: "Inter_900Black", // Use loaded font
  },
  inputContainer: {
    alignItems: "center",
  },
  inputBox: {
    backgroundColor: "white",
    borderRadius: 10,
    padding: 10,
    marginTop: 10,
    width: "100%",
  },
  submitButton: {
    backgroundColor: "#3897f0", // Match theme (can be adjusted)
    borderRadius: 10,
    padding: 15,
    marginTop: 20,
    marginBottom: 0,
    // marginRight: 0
    // marginLeft: 0,
    width: "60%",
    alignSelf: 'center',
  },
  submitText: {
    color: "white",
    textAlign: "center",
    fontSize: 18,
    fontWeight: "bold",
    fontFamily: "Inter_900Black", // Use loaded font
  },
});
