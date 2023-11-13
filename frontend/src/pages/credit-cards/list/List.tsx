import { Grid } from '@mui/material'
import React, { useEffect, useState } from 'react'
import { type CreditCard, list } from '../../../services/creditcards'
import PanelCreditCard from '../../../components/panel-credit-card/PanelCreditCard'

const List = (): React.ReactElement => {
  const [creditCards, setCreditCards] = useState<CreditCard[]>([])

  const getCreditCards = async (): Promise<void> => {
    const data = await list()
    setCreditCards(data)
  }

  useEffect(() => {
    getCreditCards().catch(error => { console.error(error) })
  }, [])

  return (
    <Grid container justifyContent={'center'} margin={2}>
        {creditCards.map((creditCard: CreditCard, i) => (<PanelCreditCard key={i} creditCard={creditCard} />))}
    </Grid>
  )
}

export default List
