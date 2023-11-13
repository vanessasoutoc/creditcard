import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'

import App from '../../../App'
import { CreditCard } from '../../../services/creditcards'

const mockFetch = (mock: CreditCard | {detail: string}): void => {
  global.fetch = jest.fn(async (): Promise<any> =>
    await Promise.resolve({
      json: async (): Promise<CreditCard | {detail: string}> => await Promise.resolve(mock)
    })
  )
}

const mockCreditCard = {
  '_id': '65512d158e4db1ec45e8d620',
  'exp_date': '01/24',
  'holder': 'Renata B Barra',
  'number': '4111 **** **** 1112',
  'cvv': '234',
  'brand': 'visa'
}

const fakeNotFound = {
  detail: 'Error CreditCard matching query does not exist.'
}

describe('Detail credit card', () => {
  it('should be not found', async () => {
    mockFetch(fakeNotFound)
    render(
      <MemoryRouter initialEntries={[`/credit-cards/${mockCreditCard._id}`]}>
        <App />
      </MemoryRouter>
    )

    expect(await screen.findByText('Cartão não encontrado.')).toBeInTheDocument()
  })

  it('should be details credit card', async () => {
    jest.mock('react-router-dom', () => ({
      ...jest.requireActual('react-router-dom'),
      useParams: () => jest.fn().mockReturnValue({ creditCardId: '65512d158e4db1ec45e8d620' }),
    }));

    mockFetch(mockCreditCard)

    render(
      <MemoryRouter initialEntries={[`/credit-cards/${mockCreditCard._id}`]}>
        <App />
      </MemoryRouter>
    )

    expect(await screen.findByText('Renata B Barra')).toBeInTheDocument()
    expect(await screen.findByText('01/24')).toBeInTheDocument()
  })
})

