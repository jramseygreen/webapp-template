import type {User} from '@/types/resources/user'

export interface Role {
  id: number;
  name: string;
  users?: User[];
}
