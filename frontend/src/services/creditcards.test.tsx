import { list, CreditCard, save } from './creditcards';

const mock_list_credit_card = [
  {
    '_id' : '6549c37d6197c9786ddd4b13',
    'number' : '4111 **** **** 1111',
    'exp_date' : '12/2023',
    'holder' : 'Vanessa Souto',
    'cvv' : '234',
    'brand' : 'visa'
  },
  {
    '_id': '654a6c71a60a16efb27f9ed9',
    'number': '4111 **** **** 1111',
    'exp_date': '12/2023',
    'holder': 'Vanessa Souto',
    'cvv': '234',
    'brand': 'visa'
  }
]

const mock_fetch = (mock: CreditCard | CreditCard[]) => {
  global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mock)
      })
    )
}

describe('CreditCards', () => {
  it('should be return list credit cards', async () => {
    mock_fetch(mock_list_credit_card)
    const result = await list()

    expect(result.length).toBeGreaterThan(1);
    expect(fetch).toBeCalled()
  })

  it('should be return create new credit card', async () => {
    const credit_card = mock_list_credit_card[0]
    // @ts-expect-error
    delete credit_card._id

    mock_fetch(mock_list_credit_card[0])
    const result = await save(credit_card)

    expect(credit_card._id).toBeFalsy()
    expect(result.brand).toEqual(mock_list_credit_card[0].brand);
    expect(fetch).toBeCalled()
  })

})


