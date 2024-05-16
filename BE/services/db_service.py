from bson import ObjectId
from .mongo_db import MongoDB

class DBService:

    def __init__(self):
        self.db = MongoDB('pulse')

    def get_pulses(self):
        pulses = self.db.read_documents('pulses', {})
        return pulses
    
    def get_pulse_by_id(self, pulse_id):
        pulse = self.db.read_document('pulses', {'_id': ObjectId(pulse_id)})
        return pulse
    
    def create_pulse(self, pulse):
        return self.db.create_document('pulses', pulse)
    
    def update_pulse(self, pulse):
        return self.db.update_document('pulses', {'_id': ObjectId(pulse.get('_id'))}, pulse)
    