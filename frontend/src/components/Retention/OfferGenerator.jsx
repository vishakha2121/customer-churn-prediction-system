import React, { useState } from 'react'
import { retentionService } from '../../services/retentionService'
import toast from 'react-hot-toast'

const OfferGenerator = ({ segmentId, onOfferGenerated }) => {
  const [loading, setLoading] = useState(false)
  const [offers, setOffers] = useState([])
  
  const generateOffers = async () => {
    setLoading(true)
    try {
      const result = await retentionService.getOffers(segmentId)
      setOffers(result.offers)
      toast.success('Offers generated successfully')
    } catch (error) {
      toast.error('Failed to generate offers')
    } finally {
      setLoading(false)
    }
  }
  
  const applyOffer = async (offerId) => {
    try {
      await retentionService.applyOffer('CUSTOMER_001', offerId)
      toast.success('Offer applied successfully')
      onOfferGenerated()
    } catch (error) {
      toast.error('Failed to apply offer')
    }
  }
  
  return (
    <div className="space-y-4">
      <button
        onClick={generateOffers}
        disabled={loading}
        className="btn-primary"
      >
        {loading ? 'Generating...' : 'Generate Offers'}
      </button>
      
      {offers.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          {offers.map((offer) => (
            <div key={offer.offer_id} className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
              <h4 className="font-semibold">{offer.offer_name}</h4>
              <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">{offer.offer_type}</p>
              <p className="text-2xl font-bold text-primary mt-2">
                {offer.offer_type === 'discount' ? `${offer.value}% OFF` : `$${offer.value}`}
              </p>
              <button
                onClick={() => applyOffer(offer.offer_id)}
                className="mt-3 text-sm text-primary hover:underline"
              >
                Apply Offer →
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default OfferGenerator