export interface CreditCard {
  _id?: string | null,
  holder: string,
  number: string,
  exp_date: string,
  cvv: string,
  brand: string
}

const apiUrl = process.env.API_URL

export const list = async (): Promise<CreditCard[]> => {
   const response = await fetch(`${apiUrl}/v1/credit-cards`,{
    method: 'GET'})
  return response.json()
}

export const save = async (data: CreditCard): Promise<CreditCard> => {
  const response = await fetch(`${apiUrl}/v1/credit-cards`,{
   method: 'POST', body: JSON.stringify(data)})
 return response.json()
}


