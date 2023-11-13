import { list, type CreditCard, save } from './creditcards'

const mockListCreditCard = [
  {
    _id: '6549c37d6197c9786ddd4b13',
    number: '4111 **** **** 1111',
    exp_date: '12/2023',
    holder: 'Vanessa Souto',
    cvv: '234',
    brand: 'visa'
  },
  {
    _id: '654a6c71a60a16efb27f9ed9',
    number: '4111 **** **** 1111',
    exp_date: '12/2023',
    holder: 'Vanessa Souto',
    cvv: '234',
    brand: 'visa'
  }
]

const mockFetch = (mock: CreditCard | CreditCard[]): void => {
  global.fetch = jest.fn(async (): Promise<any> =>
    await Promise.resolve({
      json: async (): Promise<CreditCard | CreditCard[]> => await Promise.resolve(mock)
    })
  )
}

describe('CreditCards', () => {
  it('should be return list credit cards', async () => {
    mockFetch(mockListCreditCard)
    const result = await list()

    expect(result.length).toBeGreaterThan(1)
    expect(fetch).toBeCalled()
  })

  it('should be return create new credit card', async () => {
    const creditCard = mockListCreditCard[0]
    // @ts-expect-error delete error
    delete creditCard._id

    mockFetch(mockListCreditCard[0])
    const result = await save(creditCard)

    expect(creditCard._id).toBeFalsy()
    expect(result.brand).toEqual(mockListCreditCard[0].brand)
    expect(fetch).toBeCalled()
  })
})
