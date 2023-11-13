import { Routes, Route, Outlet, Link } from 'react-router-dom'
import CreditCards from './pages/credit-cards/list/CreditCards'
import NavBar from './components/navbar/NavBar'
import React from 'react'
import { Box } from '@mui/material'
import CreditCardDetail from './pages/credit-cards/details/CreditCardDetail'

const App = (): React.ReactElement => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Home />} />
          <Route path='/credit-cards'>
            <Route path='' element={<CreditCards />} />
            <Route path=':creditCardId' element={<CreditCardDetail />} />
          </Route>
          <Route path='*' element={<NoMatch />} />
        </Route>
      </Routes>
    </div>
  )
}

const Layout = (): React.ReactElement => {
  return (
    <div>
      <NavBar />
      <Box sx={{ flexGrow: 1 }}>
          <Outlet />
      </Box>
    </div>
  )
}

const Home = (): React.ReactElement => {
  return (
    <div>
      <h2>Home</h2>
    </div>
  )
}

export const NoMatch = (): React.ReactElement => {
  return (
    <div>
      <h2>Nothing to see here!</h2>
      <p>
        <Link to='/'>Go to the home page</Link>
      </p>
    </div>
  )
}

export default App
