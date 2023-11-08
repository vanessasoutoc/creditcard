import { type ReportHandler } from 'web-vitals'

const reportWebVitals = (onPerfEntry?: ReportHandler): any => {
  if (onPerfEntry == null) {
    return
  }
  if (onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry)
      getFID(onPerfEntry)
      getFCP(onPerfEntry)
      getLCP(onPerfEntry)
      getTTFB(onPerfEntry)
    }).catch((error: Error) => {
      throw new Error(error?.message)
    })
  }
}

export default reportWebVitals
