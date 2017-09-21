class Ctrl {
    constructor(model) {
        this._nativeSearch = 'english';
        this._learningSearch = 'polish';
        this._minAge = 0;
        this._maxAge = 100;
        this._country = 'Poland';
        this.model = model;
    } 

    get nativeSearch() { return this._nativeSearch; }
    set nativeSearch(language) { this._nativeSearch = language; }
    get learningSearch() { return this._learningSearch; }
    set learningSearch(language) { this._learningSearch = language; }
    get minAge() { return this._minAge; }
    set minAge(age) { this._minAge = age; }
    get maxAge() { return this._maxAge; }
    set maxAge(age) { this._maxAge = age; }
    get country() { return this._country; }
    set country(country) { this._country = country; }

    profileSearch() {
        if (this._isValidSearchParams()) {
            var that = this;
            m.request({
                method: 'GET',
                url: 'api/profiles',
                data: {n: that._nativeSearch, l: that._learningSearch},
            })
            .then(function(result) {
                that.model.users = result;
            });
        }
    }

    profileFilter(user) {
        var countryMatch = user.country == this._country || !this.model.countries.includes(this._country);
        var ageRangeMatch = user.age >= this._minAge && user.age <= this._maxAge;
        return countryMatch && ageRangeMatch;
    }

    _isValidSearchParams() {
        return model.isValidLanguage(this.nativeSearch) &&
            model.isValidLanguage(this.learningSearch);
    }
}
