import React from 'react'
import { render, screen } from '@testing-library/react'
import CreditCards from './CreditCards'

test('renders learn react link', () => {
  render(<CreditCards />)
  const hyperText = screen.getByText(/Lista de Cartões de Crédito/i)
  expect(hyperText).toBeInTheDocument()
})
