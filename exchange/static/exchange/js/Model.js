class Model {
    constructor() {
        this.languages = [];
        this.countries = [];
        this.users = [];
        this._nativeSearch = 'english';
        this._learningSearch = 'polish';
    }

    get nativeSearch() { return this._nativeSearch; }
    set nativeSearch(language) { this._nativeSearch = language; }
    get learningSearch() { return this._learningSearch; }
    set learningSearch(language) { this._learningSearch = language; }
    
    isValidLanguage(language) {
        return this.languages.includes(language.toLowerCase());
    }

    isValidCountry(country) {
        return this.countries.includes(country.toLowerCase());
    }
}
