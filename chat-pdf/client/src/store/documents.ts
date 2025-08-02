// import axios from 'axios';
import { writable } from 'svelte/store';
import { api, getErrorMessage } from '$api';

export interface Document {
	id: string;
	file_id: string;
	name: string;
}

interface UploadStore {
	data: Document[];
	error: string;
	uploadProgress: number;
}

const INITIAL_STATE = {
	data: [],
	error: '',
	uploadProgress: 0
};

const documents = writable<UploadStore>(INITIAL_STATE);

const set = (val: Partial<UploadStore>) => {
	documents.update((state) => ({ ...state, ...val }));
};

const setUploadProgress = (event: ProgressEvent) => {
	const progress = Math.round((event.loaded / event.total) * 100);

	set({ uploadProgress: progress });
};

const upload = async (file: File) => {
	set({ error: '' });

	try {
		const formData = new FormData();
		formData.append('file', file);

		const response = await api.post('/pdfs', formData, {
			onUploadProgress: (event) => {
				// Only show up to 90% during file upload, reserve 10% for server processing
				const uploadProgress = Math.round((event.loaded / event.total) * 90);
				set({ uploadProgress });
			}
		});
		
		// Set to 100% only when the response is received
		set({ uploadProgress: 100 });
		
		return response.data;
	} catch (error) {
		set({ error: getErrorMessage(error) });
		return null;
	}
};

const getDocuments = async () => {
	const { data } = await api.get('/pdfs');
	set({ data });
};

const clearErrors = () => {
	set({ error: '', uploadProgress: 0 });
};

export { upload, getDocuments, documents, clearErrors };
