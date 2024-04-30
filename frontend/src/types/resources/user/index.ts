import type { Role } from '@/types/resources/role'

export interface User {
  id: number;
  username: string;
  is_disabled: boolean;
  roles?: Role[]
}
