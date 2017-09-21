class Ctrl {
    constructor(model, dataPopulator) {
        this._nativeSearch = 'english';
        this._learningSearch = 'polish';
        this._minAge = 0;
        this._maxAge = 100;
        this._country = 'Poland';
        this.model = model;
        this.dataPopulator = dataPopulator;
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
        this.dataPopulator.populateUsers(this.nativeSearch, this.learningSearch);
    }

    profileFilter(user) {
        var countryMatch = user.country == this._country || !this.model.countries.includes(this._country);
        var ageRangeMatch = user.age >= this._minAge && user.age <= this._maxAge;
        return countryMatch && ageRangeMatch;
    }
}
