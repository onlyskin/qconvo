class ProfileFetcher {
    constructor(model) {
        this.model = model;
    }

    populateUsers() {
        if (this._isValidSearch()) {
            var that = this;
            m.request({
                method: 'GET',
                url: 'api/profiles',
                data: {n: that.model.nativeSearch, l: that.model.learningSearch},
            })
            .then(function(result) {
                that.model.users = result;
            });
        }
    }

    _isValidSearch() {
        return this.model.isValidLanguage(this.model.nativeSearch) &&
            this.model.isValidLanguage(this.model.learningSearch);
    }
}
