export interface Detail {
  loc: [string, number]
  msg: string
  type: string
}

export interface CreditCard {
  _id?: string | null
  holder: string
  number: string
  exp_date: string
  cvv: string
  brand: string
  detail?: Detail[] | string
}

const apiUrl = process.env.REACT_APP_API_URL

export const list = async (): Promise<CreditCard[]> => {
  const response = await fetch(`${apiUrl}/v1/credit-card`, {
    method: 'GET'
  })
  return await response.json()
}

export const save = async (data: CreditCard): Promise<CreditCard> => {
  const response = await fetch(`${apiUrl}/v1/credit-card`, {
    method: 'POST', body: JSON.stringify(data)
  })
  return await response.json()
}

export const detail = async (id: string): Promise<CreditCard> => {
  const response = await fetch(`${apiUrl}/v1/credit-card/${id}`, {
    method: 'GET'
  })
  return await response.json()
}
