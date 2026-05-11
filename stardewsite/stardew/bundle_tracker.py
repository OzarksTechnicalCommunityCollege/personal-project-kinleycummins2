# Helper class - Module 7

class BundleTracker:
    SESSION_KEY = 'donated_items'

# initialize tracker w current request session
    def __init__(self, session):
        self.session = session
        if self.SESSION_KEY not in session:
            session[self.SESSION_KEY] = []

# marks a bundleitem as donated by adding id to the session list, skips if already marked donated
    def donate(self, bundle_item_id):
        if bundle_item_id not in self.session[self.SESSION_KEY]:
            self.session[self.SESSION_KEY].append(bundle_item_id)
            self.session.modified = True
            self.session.save()

# removes a bundleitem from the donated list (aka unchecking it) and then rebuilds the list
    def undonate(self, bundle_item_id):
        self.session[self.SESSION_KEY] = [
            i for i in self.session[self.SESSION_KEY] if i != bundle_item_id
        ]
        self.session.modified = True
        self.session.save()

# toggle state of the bundleitem, this is called from the toggle_item view
    def toggle(self, bundle_item_id):
        if bundle_item_id in self:
            self.undonate(bundle_item_id)
        else:
            self.donate(bundle_item_id)

# this one returns true if all bundleitems for a bundle are donated
    def is_bundle_complete(self, bundle):
        return all(item.id in self for item in bundle.bundle_items.all())

# returns how many bundles in the list are fully complete
    def completed_bundle_count(self, bundles):
        return sum(1 for b in bundles if self.is_bundle_complete(b))

# returns a precentage of bundles are the fully complete
    def percent_complete(self, bundles):
        total = len(bundles)
        if total == 0:
            return 0
        return round((self.completed_bundle_count(bundles) / total) * 100, 1)

# returns num of individual items donated so far
    def __len__(self):
        return len(self.session[self.SESSION_KEY])

# allows iterating over the donated item IDs directly
    def __iter__(self):
        return iter(self.session[self.SESSION_KEY])

# checks if a given bundleitem ID is in the donated list
    def __contains__(self, bundle_item_id):
        return bundle_item_id in self.session[self.SESSION_KEY]

# returns true if the user has donated at least one item
    def __bool__(self):
        return len(self) > 0

# compares two trackers by how many items have been donated
    def __gt__(self, other):
        return len(self) > len(other)

# returns true if two trackers have donated the same set of items
    def __eq__(self, other):
        return set(self.session[self.SESSION_KEY]) == set(other.session[self.SESSION_KEY])

