import React, { useEffect, useState } from 'react'
import { type CreditCard, detail } from '../../../services/creditcards'
import PanelCreditCard from '../../../components/panel-credit-card/PanelCreditCard'
import { useParams } from 'react-router-dom'
import AlertWarning from '../../../components/alert-warning/AlertWarning'

const Detail = (): React.ReactElement => {
  const { creditCardId } = useParams()
  const [creditCard, setCreditCard] = useState<CreditCard>()

  const detailCreditCard = async (creditCardId: string): Promise<void> => {
    const data = await detail(creditCardId)
    setCreditCard(data)
  }

  useEffect(() => {
    if (creditCardId !== null && creditCardId === undefined) {
      return
    }
    detailCreditCard(creditCardId).catch(error => { console.error(error) })
  }, [])

  return (
    <>
      {(creditCard !== null && creditCard !== undefined && creditCard.detail === undefined)
        ? <PanelCreditCard creditCard={creditCard} />
        : <AlertWarning detail="Cartão não encontrado." />}
    </>
  )
}

export default Detail
