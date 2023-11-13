import React from 'react'
import { Alert } from '@mui/material'

const AlertWarning: React.FunctionComponent<{ detail: string }> = ({ detail }) => (
  <Alert severity="warning">{detail}</Alert>
)

export default AlertWarning
