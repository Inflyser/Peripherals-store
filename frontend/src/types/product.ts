export interface Product {
  id: number
  name: string
  description: string | null
  price: number
  image_url: string | null
  category: string
  stock: number
  created_at: string
  updated_at: string | null
}

export interface ProductCreate {
  name: string
  description?: string
  price: number
  image_url?: string
  category: string
  stock?: number
}

export interface ProductUpdate {
  name?: string
  description?: string
  price?: number
  image_url?: string
  category?: string
  stock?: number
}
