import { describe, it, expect, vi } from 'vitest'
import axios from 'axios'
import { apiService, setAuthToken } from './api'

vi.mock('axios')

describe('apiService', () => {
  it('getStatus should return data', async () => {
    const mocked = axios as unknown as { get: any }
    mocked.get = vi.fn().mockResolvedValue({ data: { status: 'ok' } })
    const data = await apiService.getStatus()
    expect(data.status).toBe('ok')
  })

  it('setAuthToken sets Authorization header', () => {
    setAuthToken('abc123')
    expect((axios as any).defaults?.headers?.common['Authorization']).toContain('Bearer')
    setAuthToken(null)
  })
})
