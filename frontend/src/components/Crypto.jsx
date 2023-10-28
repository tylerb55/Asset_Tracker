import React, { useEffect, useState } from "react";
import {
    Box,
    Button,
    Flex,
    Input,
    InputGroup,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Text,
    useDisclosure
} from "@chakra-ui/react";


const CryptoContext = React.createContext({
  cryptos: [], fetchCryptos: () => {}
})

function AddCryptos() {
  const [item, setItem] = React.useState("")
  const {cryptos, fetchCryptos} = React.useContext(CryptoContext)

  const handleInput = event  => {
    setItem(event.target.value)
  }

  const handleSubmit = (event) => {
    const newCrypto = {
      "id": cryptos.length + 1,
      "item": item
    }

    fetch("http://localhost:8000/crypto", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newCrypto)
    }).then(fetchCryptos)
  }

  return (
    <form onSubmit={handleSubmit}>
      <InputGroup size="md">
        <Input
          pr="4.5rem"
          type="text"
          placeholder="Add a cryptocurrency"
          aria-label="Add a cryptocurrency"
          onChange={handleInput}
        />
      </InputGroup>
    </form>
  )
}

export default function Cryptos() {
  const [cryptos, setCryptos] = useState([])
  const fetchCryptos = async () => {
    const response = await fetch("http://localhost:8000/crypto")
    const cryptos = await response.json()
    setCryptos(cryptos.data)
  }
  useEffect(() => {
    fetchCryptos()
  }, [])
  
  return (
    <CryptoContext.Provider value={{ cryptos, fetchCryptos }}>
      <AddCryptos />
      <div>
      <h1>Cryptos</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Per Change</th>
            <th>Volume</th>
            <th>Market Cap</th>
          </tr>
        </thead>
        <tbody>
          {cryptos.map((data, index) => (
            <tr key={index}>
              <td>{data.name}</td>
              <td>{data.price}</td>
              <td>{data.per_change}</td>
              <td>{data.volume}</td>
              <td>{data.mkt_cap}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>
    </CryptoContext.Provider>
  )
}