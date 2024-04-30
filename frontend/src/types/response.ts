export interface Response<DataType = any> {
  message: string
  data: DataType
  success: boolean
  status: number
  error_type?: string
}
