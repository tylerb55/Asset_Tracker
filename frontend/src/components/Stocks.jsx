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

const StocksContext = React.createContext({
  stocks: [], fetchStocks: () => {}
})


function AddStocks() {
  const [item, setItem] = React.useState("")
  const {stocks, fetchStocks} = React.useContext(StocksContext)

  const handleInput = event  => {
    setItem(event.target.value)
  }

  const handleSubmit = (event) => {
    const newStock = {
      "id": stocks.length + 1,
      "item": item
    }

    fetch("http://localhost:8000/stock", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newStock)
    }).then(fetchStocks)
  }

  return (
    <form onSubmit={handleSubmit}>
      <InputGroup size="md">
        <Input
          pr="4.5rem"
          type="text"
          placeholder="Add a stock item"
          aria-label="Add a stock item"
          onChange={handleInput}
        />
      </InputGroup>
    </form>
  )
}


export default function Stocks() {
  const [stocks, setStocks] = useState([])
  const fetchStocks = async () => {
    const response = await fetch("http://localhost:8000/stock")
    const stocks = await response.json()
    setStocks(stocks.data)
  }
  useEffect(() => {
    fetchStocks()
  }, [])
  
  return (
    <StocksContext.Provider value={{ stocks, fetchStocks }}>
      <AddStocks />
      <div>
      <h1>Stocks</h1>
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
          {stocks.map((data, index) => (
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
    </StocksContext.Provider>
  )
}
