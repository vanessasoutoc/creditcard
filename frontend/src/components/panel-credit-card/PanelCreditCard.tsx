import React from 'react'
import { CardMedia, CardContent, Typography, CardActions, Button, Card, Grid } from '@mui/material'
import { type CreditCard } from '../../services/creditcards'

const PanelCreditCard: React.FunctionComponent<{ creditCard: CreditCard, index: number }> = ({ creditCard, index }) => (
  <Grid item margin={2} xs={3}>
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 140 }}
        image="/static/images/cards/contemplative-reptile.jpg"
        title="green iguana"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
         { creditCard.holder }
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Lizards are a widespread group of squamate reptiles, with over 6,000
          species, ranging across all continents except Antarctica
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Share</Button>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  </Grid>
)

export default PanelCreditCard
