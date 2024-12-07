import axios from 'axios';

const API_BASE_URL = "http://localhost:8000/api"; // Laravel API base URL

export interface Report {
    id?: number;
    company_name?: string; // Make fields optional for partial updates
    robot_model?: string;
    map?: string;
    route?: string;
    orientations_tried?: number;
    runs?: number;
    confidence?: number;
    time_spent?: number;
    predicted_route_time?: number;
    boxes_moved_per_run?: number;
}

// Save a new Report
export const saveReport = async (report: Report): Promise<Report> => {
    const response = await axios.post(`${API_BASE_URL}/report`, report, {
        headers: {
            'Content-Type': 'application/json', // Set content type to JSON
        }
    });
    return response.data; // Return the saved Report object, including its ID
};

// Get all Reports
export const getReports = async (): Promise<Report[]> => {
    const response = await axios.get(`${API_BASE_URL}/report`);
    return response.data;
};

// Update an existing Report by ID
export const updateReport = async (id: number, partialReport: Partial<Report>): Promise<Report> => {
    const response = await axios.patch(`${API_BASE_URL}/report/${id}`, partialReport, {
        headers: {
            'Content-Type': 'application/json', // Set content type to JSON
        }
    });
    return response.data;
};
