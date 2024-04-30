export interface Column {
  name: string;
  key?: string;
}

export interface Record {
  id: string | number;
  [key: string]: any;
}
