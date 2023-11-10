import React from 'react'
import { type CreditCard } from '../../services/creditcards'
import './detail-credit-card.css'
import { Typography } from '@mui/material'

const DetailCreditCard: React.FunctionComponent<{ creditCard: CreditCard }> = ({ creditCard }) => (
  <div className={`credit-card selectable ${creditCard.brand}`}>
    <div className='inline'>
      <div className="credit-card-last4">
        {creditCard.number}
      </div>
      <Typography gutterBottom variant="subtitle2" component="div">
         { creditCard.holder }
      </Typography>
    </div>
    <div className="credit-card-expiry">
      {creditCard.exp_date}
    </div>
  </div>
)

export default DetailCreditCard
