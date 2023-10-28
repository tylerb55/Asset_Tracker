import React from "react";
import { render } from 'react-dom';
import { ChakraProvider } from "@chakra-ui/react";

import Header from "./components/Header";
import Stocks from "./components/Stocks";
import Crypto from "./components/Crypto";

function App() {
  return (
    <ChakraProvider>
      <Header />
      <Stocks />
      <Crypto />
    </ChakraProvider>
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
