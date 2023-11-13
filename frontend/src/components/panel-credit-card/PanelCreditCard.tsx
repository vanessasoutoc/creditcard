import React from 'react'
import { CardActions, Button, Card, Grid } from '@mui/material'
import { type CreditCard } from '../../services/creditcards'
import DetailCreditCard from '../detail-credit-card/DetailCreditCard'

const PanelCreditCard: React.FunctionComponent<{ creditCard: CreditCard }> = ({ creditCard }) => (
  <Grid item margin={1} xs={12} sm={4} md={4} lg={3} xl={2}>
    <Card sx={{ maxWidth: 340 }}>
      <DetailCreditCard key="detail-credit-card" creditCard={creditCard} />
      <CardActions style={{ justifyContent: 'end' }} >
        <Button size="small">Ver detalhes</Button>
      </CardActions>
    </Card>
  </Grid>
)

export default PanelCreditCard
