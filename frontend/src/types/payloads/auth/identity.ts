export interface CreateIdentityPayload {
  username: string
  password: string
}

export interface UpdateIdentityPayload {
  username?: string
  new_password?: string
  password: string
}

export interface DeleteIdentityPayload {
  password: string
}
