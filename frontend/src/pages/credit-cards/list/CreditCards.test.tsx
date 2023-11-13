import { render, screen } from '@testing-library/react'
import { CreditCard } from '../../../services/creditcards'
import { MemoryRouter } from 'react-router-dom'
import App from '../../../App'

const mockFetch = (mock: CreditCard[] | []): void => {
  global.fetch = jest.fn(async (): Promise<any> =>
    await Promise.resolve({
      json: async (): Promise<CreditCard[] | []> => await Promise.resolve(mock)
    })
  )
}

const mockCreditCard = [{
  '_id': '65512d158e4db1ec45e8d620',
  'exp_date': '01/24',
  'holder': 'Renata B Barra',
  'number': '4111 **** **** 1112',
  'cvv': '234',
  'brand': 'visa'
}]

const fakeNotFound = {
  detail: 'Error CreditCard matching query does not exist.'
}

describe('list', () => {
  it('should be list credit card', async() => {
    mockFetch(mockCreditCard)
    render(
      <MemoryRouter initialEntries={[`/credit-cards`]}>
        <App />
      </MemoryRouter>
    )

    expect(await screen.findByText('Renata B Barra')).toBeInTheDocument()
  })
})
