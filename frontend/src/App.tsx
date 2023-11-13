import { Routes, Route, Outlet, Link, Navigate } from 'react-router-dom'
import List from './pages/credit-cards/list/List'
import NavBar from './components/navbar/NavBar'
import React from 'react'
import { Box, Grid } from '@mui/material'
import Detail from './pages/credit-cards/detail/Detail'

const App = (): React.ReactElement => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Navigate to="/credit-cards" />}/>
          <Route path='/credit-cards'>
            <Route path='' element={<List />} />
            <Route path=':creditCardId' element={<Detail />} />
          </Route>
          <Route path='*' element={<NoMatch />} />
        </Route>
      </Routes>
    </div>
  )
}

const Layout = (): React.ReactElement => {
  return (
    <>
      <NavBar />
      <Box sx={{ flexGrow: 1 }}>
        <Grid container justifyContent={'center'} margin={2}>
          <Outlet />
        </Grid>
      </Box>
    </>
  )
}

export const NoMatch = (): React.ReactElement => {
  return (
    <>
      <h2>Página não encontrada</h2>
      <p>
        <Link to='/'>Volte para a Home</Link>
      </p>
    </>
  )
}

export default App
