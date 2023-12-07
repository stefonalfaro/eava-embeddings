//LangChain Embedding Abstraction for use with custom implementation

export class eavaEmbeddings extends Embeddings {
    url:string
    apiKey?:string
    constructor(_url:string, _apiKey?:string){
        const fieldsWithDefaults = { };
        super(fieldsWithDefaults);

        this.url = _url;
        if (_apiKey)
            this.apiKey = _apiKey;
    }

    async embedDocuments(documents: string[]): Promise<number[][]> {
        const data = JSON.stringify({ "sentences": documents });

        const config = {
            method: 'post',
            maxBodyLength: Infinity,
            url: this.url,
            headers: { 'Content-Type': 'application/json' },
            data: data,
        };

        try 
        {
            const response = await axios.request(config);
            //console.log(JSON.stringify(response.data));
            return response.data;
        } 
        catch (error) 
        {
            console.error(error);
            throw error;
        }
    }

    async embedQuery(document: string): Promise<number[]> {
        const data = JSON.stringify({ "sentences": [document] });

        const  config = {
            method: 'post',
            maxBodyLength: Infinity,
            url: this.url,
            headers: { 'Content-Type': 'application/json'},
            data : data
        };

        try 
        {
            const response = await axios.request(config);
            //console.log(JSON.stringify(response.data));
            return response.data[0];
        } 
        catch (error)
        {
            console.error(error);
            throw error;
        }
    }
}