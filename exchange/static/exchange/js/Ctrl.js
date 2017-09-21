class Ctrl {
    constructor(model, dataPopulator) {
        this._minAge = 0;
        this._maxAge = 100;
        this._country = 'Poland';
        this.model = model;
        this.dataPopulator = dataPopulator;
    } 

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
        var countryMatch = user.country == this.country || !this.model.isValidCountry(this.country);
        var ageRangeMatch = user.age >= this.minAge && user.age <= this.maxAge;
        return countryMatch && ageRangeMatch;
    }
}
