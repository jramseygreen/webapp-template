export interface CreateUserPayload {
  username: string;
  password: string
  is_disabled?: boolean
  roles?: string[]
}

export interface UpdateUserPayload {
  id: number;
  username?: string
  password?: string
  is_disabled?: boolean
  roles?: string[]
}
